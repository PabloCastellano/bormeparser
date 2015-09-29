#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .acto import ACTO
#from .download import download_pdf
from .download import get_url_pdf, BORME_PDF_URL, get_url_xml
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
            raise ValueError
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
            raise ValueError(name)
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
            raise ValueError
        self.name = name

    def _set_value(self, value):
        if value != True:
            raise ValueError('value must be True: %s' % value)
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


class BormeXML(object):

    def __init__(self):
        self._url = None
        self.date = None
        self.filename = None

    def _load(self, source):
        def parse_date(fecha):
            return datetime.datetime.strptime(fecha, '%d/%m/%Y').date()

        self.xml = etree.parse(source)
        if self.xml.getroot().tag != 'sumario':
            raise BormeDoesntExistException

        self.date = parse_date(self.xml.xpath('//sumario/meta/fecha')[0].text)
        self.nbo = int(self.xml.xpath('//sumario/diario')[0].attrib['nbo'])  # Número de Boletín Oficial
        self.prev_borme = parse_date(self.xml.xpath('//sumario/meta/fechaAnt')[0].text)
        self.next_borme = parse_date(self.xml.xpath('//sumario/meta/fechaSig')[0].text)

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
                raise ValueError('File not found: %s' % path)
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



# TODO: Iterador de anuncios
# TODO: Info
# TODO: Create instance directly from filename
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
        self.info = {}
        self._set_anuncios(anuncios)
        self._url = None
        if not lazy:
            self._set_url()

    @classmethod
    def from_file(cls, filename):
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

    def get_info(self):
        #borme['info'] = {'pages': 5, 'anuncios': 38, 'fromanuncio': 12222, 'toanuncio': 12260}
        #return self.info
        raise NotImplementedError

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
        doc['filename'] = self.filename
        doc['info'] = self.info
        doc['anuncios'] = {}

        for id, anuncio in self.anuncios.items():
            doc['anuncios'][anuncio.id] = OrderedDict()
            doc['anuncios'][anuncio.id]['empresa'] = anuncio.empresa
            doc['anuncios'][anuncio.id]['datos registrales'] = anuncio.datos_registrales
            doc['anuncios'][anuncio.id]['actos'] = {}
            for acto in anuncio.actos:
                doc['anuncios'][anuncio.id]['actos'][acto.name] = acto.value

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
