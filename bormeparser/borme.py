#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .acto import ACTO
#from .download import download_pdf
from .download import get_url_pdf, URL_BASE, get_url_xml, download_url, download_urls_multi
#from .exceptions import BormeInvalidActoException
from .exceptions import BormeAlreadyDownloadedException, BormeAnuncioNotFound, BormeDoesntExistException
from .regex import is_acto_cargo, is_acto_noarg, is_acto_rare_cargo
#from .parser import parse as parse_borme
#from .seccion import SECCION
from .provincia import Provincia
import datetime
import logging
import json
import os
import six

from lxml import etree
from collections import OrderedDict

try:
    FileNotFoundError
except NameError:
    # Python 2
    FileNotFoundError = IOError

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
logger.addHandler(ch)
logger.setLevel(logging.WARN)


class BormeActo(object):
    """
    Representa un Acto del Registro Mercantil. Instanciar BormeActoTexto o BormeActoCargo
    """
    def __init__(self, name, value):
        logger.debug('new %s(%s): %s' % (self.__class__.__name__, name, value))
        if name not in ACTO.ALL_KEYWORDS:
            logger.warning('Invalid acto found: %s' % name)
            #raise BormeInvalidActoException('Invalid acto found: %s' % acto_nombre)
        self._set_name(name)
        self._set_value(value)

    # TODO: @classmethod para elegir automaticamente el tipo?

    def _set_name(self, name):
        raise NotImplementedError

    def _set_value(self, value):
        raise NotImplementedError

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return "<%s(%s): %s>" % (self.__class__.__name__, self.name, self.value)


class BormeActoTexto(BormeActo):
    """
    Representa un Acto del Registro Mercantil con atributo de cadena de texto.
    """

    def _set_name(self, name):
        if is_acto_cargo(name) or is_acto_rare_cargo(name):
            raise ValueError('No se puede BormeActoTexto con un acto de cargo: %s' % name)
        self.name = name

    def _set_value(self, value):
        if not isinstance(value, six.string_types):
            raise ValueError('value must be str: %s' % value)
        self.value = value


class BormeActoCargo(BormeActo):
    """
    Representa un Acto del Registro Mercantil con atributo de lista de cargos y nombres.
    """

    def _set_name(self, name):
        if not is_acto_cargo(name) and not is_acto_rare_cargo(name):
            raise ValueError('No se puede BormeActoCargo sin un acto de cargo: %s' % name)
        self.name = name

    def _set_value(self, value):
        if not isinstance(value, dict):
            raise ValueError('value must be dict: %s' % value)

        for _, v in value.items():
            if not isinstance(v, set):
                raise ValueError('v must be set: %s' % v)

        self.value = value

    @property
    def cargos(self):
        return self.value

    def get_nombres_cargos(self):
        return list(self.value.keys())


class BormeActoFact(BormeActo):

    def _set_name(self, name):
        if not is_acto_noarg(name):
            raise ValueError('No se puede BormeActoFact sin un acto de sin argumento: %s' % name)
        self.name = name

    def _set_value(self, value):
        if value is not True:
            logger.warning('value must be True: %s' % value)
            #raise ValueError('value must be True: %s' % value)
        self.value = value


class BormeAnuncio(object):
    """
    Representa un anuncio con un conjunto de actos mercantiles (Constitucion, Nombramientos, ...)
    """

    def __init__(self, id, empresa, actos):
        logger.debug('new BormeAnuncio(%s) %s' % (id, empresa))
        self.id = id
        self.empresa = empresa
        self.datos_registrales = ""
        self._set_actos(actos.copy())

    def _set_actos(self, actos):
        self.actos = []
        self.datos_registrales = actos['Datos registrales']
        del actos['Datos registrales']

        for acto_nombre, valor in actos.items():
            if is_acto_cargo(acto_nombre) or is_acto_rare_cargo(acto_nombre):
                a = BormeActoCargo(acto_nombre, valor)
                self.actos.append(a)
            elif is_acto_noarg(acto_nombre):
                a = BormeActoFact(acto_nombre, valor)
                self.actos.append(a)
            else:
                a = BormeActoTexto(acto_nombre, valor)
                self.actos.append(a)

    def get_borme_actos(self):
        return self.actos

    def get_actos(self):
        for acto in self.actos:
            yield acto.name, acto.value

    def __repr__(self):
        return "<BormeAnuncio(%d) %s (%d)>" % (self.id, self.empresa, len(self.actos))


# TODO: guardar self.filepath si from_file, y si from_date y luego save_to_file tb
class BormeXML(object):

    def __init__(self):
        self._url = None
        self.date = None
        self.filename = None
        self._urls_seccion = None
        self._urls_provincia = None

    def _load(self, source):
        def parse_date(fecha):
            return datetime.datetime.strptime(fecha, '%d/%m/%Y').date()

        self.xml = etree.parse(source)
        if self.xml.getroot().tag != 'sumario':
            raise BormeDoesntExistException

        self.date = parse_date(self.xml.xpath('//sumario/meta/fecha')[0].text)
        self.nbo = int(self.xml.xpath('//sumario/diario')[0].attrib['nbo'])  # Número de Boletín Oficial
        self.prev_borme = parse_date(self.xml.xpath('//sumario/meta/fechaAnt')[0].text)
        next_borme = self.xml.xpath('//sumario/meta/fechaSig')[0].text
        if next_borme:
            self.next_borme = parse_date(next_borme)
            self.is_final = True
        else:
            self.next_borme = None
            self.is_final = False
            logger.warning('Está accediendo un archivo BORME XML no definitivo')

    @property
    def url(self):
        if not self._url:
            self._url = get_url_xml(self.date)
        return self._url

    @staticmethod
    def from_file(path):
        bxml = BormeXML()

        if not path.startswith('http'):
            if not os.path.exists(path):
                raise FileNotFoundError(path)
            bxml.filename = path

        bxml._load(path)
        return bxml

    @staticmethod
    def from_date(date):
        if isinstance(date, tuple):
            date = datetime.date(year=date[0], month=date[1], day=date[2])

        url = get_url_xml(date)
        bxml = BormeXML()
        bxml._url = url
        bxml._load(url)
        assert(date == bxml.date)
        return bxml

    def get_url_pdfs(self, date, seccion=None, provincia=None):
        if seccion and not provincia:
            urls = self._get_url_pdfs_seccion(seccion)
        elif provincia and not seccion:
            urls = self._get_url_pdfs_provincia(provincia)
        elif provincia and seccion:
            raise NotImplementedError
        else:
            raise AttributeError('You must specifiy either provincia or seccion or both')
        return urls

    def _get_url_pdfs_provincia(self, provincia):
        """ Obtiene las URLs para descargar los BORMEs de la provincia y fecha indicada """

        if not self._urls_provincia:
            self._urls_provincia = {}
            for item in self.xml.xpath('//sumario/diario/seccion/emisor/item'):
                prov = item.xpath('titulo')[0].text
                if prov != provincia:
                    continue
                url = URL_BASE + item.xpath('urlPdf')[0].text
                seccion = item.getparent().getparent().get('num')
                self._urls_provincia[seccion] = url

        return self._urls_provincia

    def _get_url_pdfs_seccion(self, seccion):
        """ Obtiene las URLs para descargar los BORMEs de la seccion y fecha indicada """

        if not self._urls_seccion:
            self._urls_seccion = {}
            for item in self.xml.xpath('//sumario/diario/seccion[@num="%s"]/emisor/item' % seccion):
                provincia = item.xpath('titulo')[0].text
                url = URL_BASE + item.xpath('urlPdf')[0].text
                self._urls_seccion[provincia] = url

        return self._urls_seccion

    def download_pdfs(self, path, provincia=None, seccion=None):
        """ Descarga BORMEs PDF de las provincia, la seccion y la fecha indicada """
        urls = self.get_url_pdfs(self.date, provincia=provincia, seccion=seccion)
        files = download_urls_multi(urls, path)
        return True, files

    def download_pdf(self, filename, seccion, provincia):
        """ Descarga BORME PDF de la provincia, la seccion y la fecha indicada """
        url = get_url_pdf(self.date, seccion, provincia)
        downloaded = download_url(url, filename)
        return downloaded

    # TODO: Obtener versión definitiva si ya ha sido publicado el próximo BORME
    def save_to_file(self, path):
        """ Guarda el archivo XML en disco. Útil cuando se genera el XML a partir de una fecha. """
        # El archivo generado es diferente. Se corrige manualmente:
        #   en la cabecera XML usa " en lugar de '
        #   <fechaSig/> en lugar de <fechaSig></fechaSig>

        self.xml.write(path, encoding='iso-8859-1', pretty_print=True)
        with open(path, 'r', encoding='iso-8859-1') as fp:
            content = fp.read()

        content = content.replace("<?xml version='1.0' encoding='ISO-8859-1'?>", '<?xml version="1.0" encoding="ISO-8859-1"?>')
        if not self.is_final:
            logger.warning('Está guardando un archivo no definitivo')
            content = content.replace('<fechaSig/>', '<fechaSig></fechaSig>')

        with open(path, 'w', encoding='iso-8859-1') as fp:
            fp.write(content)
        return True


class Borme(object):

    def __init__(self, date, seccion, provincia, num, cve, anuncios=None, filename=None, lazy=True):
        if isinstance(date, tuple):
            date = datetime.date(year=date[0], month=date[1], day=date[2])
        self.date = date
        self.seccion = seccion
        self.provincia = provincia
        self.num = num
        self.cve = cve
        self.filename = filename
        self._parsed = False
        self.num_pages = 0  # TODO
        self._set_anuncios(anuncios)
        self._url = None
        if not lazy:
            self._set_url()

    @classmethod
    def from_file(cls, filename):
        # TODO: Create instance directly from filename
        raise NotImplementedError

    def _set_anuncios(self, anuncios):
        self.anuncios = OrderedDict()
        for anuncio in anuncios:
            self.anuncios[anuncio.id] = anuncio
        self.anuncios_rango = (anuncios[0].id, anuncios[-1].id)

    def _set_url(self):
        self._url = get_url_pdf(self.date, self.seccion, self.provincia)

    @property
    def url(self):
        if not self._url:
            self._set_url()
        return self._url

    def get_anuncio(self, anuncio_id):
        try:
            return self.anuncios[anuncio_id]
        except KeyError:
            raise BormeAnuncioNotFound('Anuncio %d not found in BORME %s' % (anuncio_id, str(self)))

    def get_anuncios_ids(self):
        """
        [BormeAnuncio]
        """
        return list(self.anuncios.values())

    def get_anuncios(self):
        """
        [BormeAnuncio]
        """
        return list(self.anuncios.values())

    def download(self, filename):
        if self.filename is not None:
            raise BormeAlreadyDownloadedException(filename)
        downloaded = download_pdf(self.date, filename, self.seccion, self.provincia)
        if downloaded:
            self.filename = filename
        return downloaded

    def _to_dict(self):
        doc = OrderedDict()
        doc['cve'] = self.cve
        doc['date'] = self.date.isoformat()
        doc['seccion'] = self.seccion
        doc['provincia'] = self.provincia
        doc['num'] = self.num
        doc['url'] = self._url
        doc['from_anuncio'] = self.anuncios_rango[0]
        doc['to_anuncio'] = self.anuncios_rango[1]
        doc['anuncios'] = {}

        num_anuncios = 0
        for id, anuncio in self.anuncios.items():
            num_anuncios += 1
            doc['anuncios'][anuncio.id] = OrderedDict()
            doc['anuncios'][anuncio.id]['empresa'] = anuncio.empresa
            doc['anuncios'][anuncio.id]['datos registrales'] = anuncio.datos_registrales
            doc['anuncios'][anuncio.id]['actos'] = {}
            doc['anuncios'][anuncio.id]['num_actos'] = 0
            for acto in anuncio.actos:
                doc['anuncios'][anuncio.id]['num_actos'] += 1
                doc['anuncios'][anuncio.id]['actos'][acto.name] = acto.value

        doc['num_anuncios'] = num_anuncios
        logger.debug(doc)
        return doc

    def to_json(self, filename, overwrite=True, pretty=True):
        def set_default(obj):
            """ serialize Python sets as lists
                http://stackoverflow.com/a/22281062
            """
            if isinstance(obj, set):
                return list(obj)
            elif isinstance(obj, Provincia):
                return str(obj)
            raise TypeError(type(obj))

        if os.path.isfile(filename) and not overwrite:
            return False

        doc = self._to_dict()
        indent = 2 if pretty else None
        with open(filename, 'w') as fp:
            fp.write(json.dumps(doc, default=set_default, indent=indent))
        return True

    @classmethod
    def from_json(self, filename):
        raise NotImplementedError

    def __lt__(self, other):
        return self.anuncios_rango[1] < other.anuncios_rango[0]

    def __repr__(self):
        return "<Borme(%s) seccion:%s provincia:%s>" % (self.date, self.seccion, self.provincia)
