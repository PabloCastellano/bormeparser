#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# borme.py -
# Copyright (C) 2015-2017 Pablo Castellano <pablo@anche.no>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from .acto import ACTO
from .download import (
        get_url_pdf, URL_BASE, get_url_xml,
        download_url, download_urls_multi, USE_HTTPS,
        download_urls_multi_names, get_url_pdf_from_xml,
        download_pdf)
# from .exceptions import BormeInvalidActoException
from .exceptions import (
        BormeAlreadyDownloadedException,
        BormeAnuncioNotFound,
        BormeDoesntExistException)
from .regex import is_acto_cargo
# from .parser import parse as parse_borme
from .seccion import SECCION
from .provincia import Provincia, PROVINCIA
from .utils import get_borme_xml_filepath

import datetime
import io
import json
import logging
import os.path
import os
import re
import requests

from lxml import etree

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
logger.addHandler(ch)
logger.setLevel(logging.WARN)

# RAW_FILE_VERSION must be a positive integer string.
# Each new version adds 1 if the result file can change.
RAW_FILE_VERSION = "1"
# Thousands file version. It represents the file version part corresponding
# to this parser
TH_FILE_VERSION = "2"
# The file version depends on parser one and parser two. It is coded to avoid
# that the parser one changes and the parser two does not.
FILE_VERSION = "{}".format(int(RAW_FILE_VERSION) + 1000 * int(TH_FILE_VERSION))


class BormeActo(object):
    """Representa un Acto del Registro Mercantil. Instanciar BormeActoTexto
       o BormeActoCargo
    """
    def __init__(self, name, value):
        logger.debug('new %s(%s): %s' % (self.__class__.__name__, name, value))
        if name not in ACTO.ALL_KEYWORDS:
            logger.warning('Invalid acto found: %s' % name)
            # raise BormeInvalidActoException(
            #       'Invalid acto found: %s' % acto_nombre)
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
        return "<{}({}): {}>".format(
                self.__class__.__name__, self.name, self.value)


class BormeActoTexto(BormeActo):
    """
    Representa un Acto del Registro Mercantil con atributo de cadena de texto.
    """

    def _set_name(self, name):
        if is_acto_cargo(name):
            raise ValueError(
                'No se puede BormeActoTexto con un acto de cargo: %s' % name)
        self.name = name

    def _set_value(self, value):
        if not (value is None or isinstance(value, str)):
            raise ValueError('value must be str or None: %s' % value)
        self.value = value


class BormeActoCargo(BormeActo):
    """Representa un Acto del Registro Mercantil con atributo de lista de
       cargos y nombres.
    """

    def _set_name(self, name):
        if not is_acto_cargo(name):
            raise ValueError(
                'No se puede BormeActoCargo sin un acto de cargo: %s' % name)
        self.name = name

    def _set_value(self, value):
        if not isinstance(value, dict):
            raise ValueError('value must be a dictionary: %s' % value)

        for k, v in value.items():
            if not isinstance(v, set):
                if isinstance(v, list):
                    value[k] = set(v)
                else:
                    raise ValueError('v must be a set: %s' % v)

        self.value = value

    @property
    def cargos(self):
        return self.value

    def get_nombres_cargos(self):
        return list(self.value.keys())


class BormeAnuncio(object):
    """Representa un anuncio con un conjunto de actos mercantiles
       (Constitucion, Nombramientos, ...)
    """

    def __init__(self, id, empresa, actos, extra, datos_registrales=None):
        logger.debug("new BormeAnuncio({}) {} ({})".format(id, empresa, extra))
        self.id = id
        self.empresa = empresa
        self.registro = extra["registro"]
        self.sucursal = extra["sucursal"]
        self.liquidacion = extra["liquidacion"]
        self.datos_registrales = datos_registrales or ""
        self._set_actos(actos)

    def _set_actos(self, actos):
        self.actos = []
        for acto in actos:
            for acto_nombre, valor in acto.items():
                if acto_nombre == 'Datos registrales':
                    self.datos_registrales = valor
                    continue

                if is_acto_cargo(acto_nombre):
                    a = BormeActoCargo(acto_nombre, valor)
                else:
                    a = BormeActoTexto(acto_nombre, valor)
                self.actos.append(a)

    def get_borme_actos(self):
        return self.actos

    def get_actos(self):
        for acto in self.actos:
            yield acto.name, acto.value

    def __repr__(self):
        return "<BormeAnuncio({}) {} (r:{}, s:{}, l:{}) ({})>".format(
                    self.id, self.empresa, self.registro, self.sucursal,
                    self.liquidacion, len(self.actos))


# TODO: guardar self.filepath si from_file,
# y si from_date y luego save_to_file tb
class BormeXML(object):

    def __init__(self):
        self._url = None
        self.date = None
        self.filename = None

    def _load(self, source):
        def parse_date(fecha):
            return datetime.datetime.strptime(fecha, '%d/%m/%Y').date()

        if source.startswith('http'):
            req = requests.get(source)
            content = req.text.encode("ISO-8859-1")
            self.xml = etree.fromstring(content).getroottree()
        else:
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
            logger.warning(
                'Está accediendo un archivo BORME XML no definitivo')

    @property
    def url(self):
        if not self._url:
            self._url = get_url_xml(self.date, secure=self.use_https)
        return self._url

    @staticmethod
    def from_file(path, secure=USE_HTTPS):
        bxml = BormeXML()
        bxml.use_https = secure

        if not path.startswith('http'):
            if not os.path.exists(path):
                raise IOError(path)
            bxml.filename = path

        bxml._load(path)
        return bxml

    @staticmethod
    def from_date(date, secure=USE_HTTPS):
        if isinstance(date, tuple):
            date = datetime.date(year=date[0], month=date[1], day=date[2])

        url = get_url_xml(date)
        bxml = BormeXML()
        bxml.use_https = secure
        bxml._url = url
        bxml._load(url)
        assert(date == bxml.date)
        return bxml

    def get_urls_cve(self, seccion=None, provincia=None):
        protocol = 'https' if self.use_https else 'http'
        url_base = URL_BASE % protocol
        urls_cve = {}

        for item in self._build_xpath(seccion, provincia):
            cve = item.get('id')
            url = url_base + item.xpath('urlPdf')[0].text
            urls_cve[cve] = url
        return urls_cve

    def get_url_pdfs(self, seccion=None, provincia=None):
        """Obtiene urls para descargar BORME.

        Debe especificar seccion, provincia, o ambas.
        Para seccion='C', provincia no se tiene en cuenta.
        """
        if seccion == SECCION.C:
            if provincia:
                logger.warn(
                    'provincia parameter makes no sense when seccion="C"')
            urls = self._get_url_borme_c(format='xml')
        else:
            urls = self._get_url_borme_a(seccion=seccion, provincia=provincia)
        return urls

    def get_cves(self, seccion=None, provincia=None):
        """ Obtiene los CVEs """

        cves = []
        for item in self._build_xpath(seccion, provincia):
            if not item.get('id').endswith('-99'):
                cves.append(item.get('id'))
        if len(cves) == 1:
            cves = cves[0]
        return cves

    def get_sizes(self, seccion=None, provincia=None):
        """ Obtiene un diccionario con el CVE y su tamaño """

        sizes = {}
        for item in self._build_xpath(seccion, provincia):
            if not item.get('id').endswith('-99'):
                cve = item.get('id')
                size = item.xpath('urlPdf')[0].get('szBytes')
                sizes[cve] = int(size)
        return sizes

    def get_provincias(self, seccion):
        xpath = '//sumario/diario/seccion[@num="{}"]/emisor/item/titulo/text()'.format(seccion)
        provincias = self.xml.xpath(xpath)
        provincias.remove("ÍNDICE ALFABÉTICO DE SOCIEDADES")
        return provincias

    # TODO: Los nombres en el XML vienen en sus respectivos idiomas
    # Mientras que PROVINCIA.provincia.GERONA no retornaría nada
    def _build_xpath(self, seccion=None, provincia=None):
        """
            Devuelve una lista con los elementos item
        """
        if seccion and provincia:
            xpath = '//sumario/diario/seccion[@num="{}"]/emisor/item/titulo[text()="{}"]'.format(seccion, provincia)
        elif seccion:
            xpath = '//sumario/diario/seccion[@num="{}"]/emisor/item'.format(seccion)
        elif provincia:
            xpath = '//sumario/diario/seccion/emisor/item/titulo[text()="{}"]'.format(provincia)
        else:
            xpath = '//sumario/diario/seccion/emisor/item'

        if provincia:
            return [item.getparent() for item in self.xml.xpath(xpath)]
        else:
            return self.xml.xpath(xpath)

    def _get_url_borme_c(self, format='xml'):
        """Obtiene las URLs para descargar los BORMEs de la seccion C y la
           fecha indicada.

           El parámetro format puede ser: 'xml', 'html' o 'pdf'
        """

        protocol = 'https' if self.use_https else 'http'
        url_base = URL_BASE % protocol
        urls = {}

        xpath_query = '//sumario/diario/seccion[@num="C"]/emisor/item'
        for item in self.xml.xpath(xpath_query):
            if format == 'xml':
                url = url_base + item.xpath('urlXml')[0].text
            elif format in ('htm', 'html'):
                url = url_base + item.xpath('urlHtm')[0].text
            elif format == 'pdf':
                url = url_base + item.xpath('urlPdf')[0].text
            cve = item.get('id')
            filename = '{}.{}'.format(cve, format)
            urls[filename] = url

        return urls

    def _get_url_borme_a(self, seccion=None, provincia=None):
        """
            Obtiene las URLs para descargar los BORMEs de la provincia,
            sección y fecha indicada.

            Devuelve urls: {provincia: url_seccion}
                           {seccion: url_provincia}
                           {cve: url_seccion_provincia}

        """
        if not seccion and not provincia:
            raise AttributeError(
                    'You must specifiy either provincia or seccion or both')

        protocol = 'https' if self.use_https else 'http'
        url_base = URL_BASE % protocol
        urls = {}

        for item in self._build_xpath(seccion, provincia):
            if seccion and provincia:
                key = item.get('id')  # cve
            elif seccion:
                key = item.xpath('titulo')[0].text  # provincia
            elif provincia:
                key = item.getparent().getparent().get('num')  # seccion
            url = url_base + item.xpath('urlPdf')[0].text
            urls[key] = url

        return urls

    def download_borme(self, path, provincia=None, seccion=None):
        """ Descarga BORMEs PDF de las provincia, la seccion y la fecha indicada
        """
        urls = self.get_url_pdfs(provincia=provincia, seccion=seccion)
        if seccion == SECCION.C:
            files = download_urls_multi_names(urls, path)
        else:
            files = download_urls_multi(urls, path)
        return True, files

    def download_single_borme(self, filename, seccion, provincia):
        """ Descarga BORME PDF de la provincia, la seccion y la fecha indicada
        """
        url = get_url_pdf(self.date, seccion, provincia)
        downloaded = download_url(url, filename)
        return downloaded

    # TODO: Obtener versión definitiva si ya ha sido publicado el próximo BORME
    def save_to_file(self, path):
        """ Guarda el archivo XML en disco.

        Útil cuando se genera el XML a partir de una fecha.
        """
        # El archivo generado es diferente. Se corrige manualmente:
        #   en la cabecera XML usa " en lugar de '
        #   <fechaSig/> en lugar de <fechaSig></fechaSig>

        # el path puede no existir ya que es de una fecha anterior.
        if not os.path.isdir(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        self.xml.write(path, encoding='iso-8859-1', pretty_print=True)

        with open(path, 'r', encoding='iso-8859-1') as fp:
            content = fp.read()

        # Reemplaza comillas simples
        content = content.replace(
                    "<?xml version='1.0' encoding='ISO-8859-1'?>",
                    '<?xml version="1.0" encoding="ISO-8859-1"?>')
        if not self.is_final:
            logger.warning('Está guardando un archivo no definitivo')
            content = content.replace('<fechaSig/>', '<fechaSig></fechaSig>')

        with open(path, 'w', encoding='iso-8859-1') as fp:
            fp.write(content)

        return True


class Borme(object):

    def __init__(self, date, seccion, provincia, num, cve, anuncios=None,
                 filename=None, lazy=True):
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
        """
            anuncios: [BormeAnuncio]
        """
        self.anuncios = {}
        for anuncio in anuncios:
            self.anuncios[anuncio.id] = anuncio
        self.anuncios_rango = (min(self.anuncios.keys()),
                               max(self.anuncios.keys()))

    def _set_url(self):
        xml_path = get_borme_xml_filepath(self.date)
        if os.path.isfile(xml_path):
            self._url = get_url_pdf_from_xml(self.date, self.seccion,
                                             self.provincia, xml_path)
        else:
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
            raise BormeAnuncioNotFound(
                'Anuncio {} not found in BORME {}'.format(
                    anuncio_id, str(self)))

    def get_anuncios_ids(self):
        """
        [BormeAnuncio]
        """
        return sorted(self.anuncios.keys())

    def get_anuncios(self):
        """
        [BormeAnuncio]
        """
        return list(self.anuncios.values())

    def download(self, filename):
        if self.filename is not None:
            raise BormeAlreadyDownloadedException(filename)
        downloaded = download_pdf(self.date, filename, self.seccion,
                                  self.provincia)
        if downloaded:
            self.filename = filename
        return downloaded

    def _to_dict(self, set_url=True):
        doc = {
            'cve': self.cve,
            'date': self.date.isoformat(),
            'seccion': self.seccion,
            'provincia': self.provincia,
            'num': self.num,
            'from_anuncio': self.anuncios_rango[0],
            'to_anuncio': self.anuncios_rango[1],
            'anuncios': {}
        }

        num_anuncios = 0
        for id, anuncio in self.anuncios.items():
            doc['anuncios'][anuncio.id] = {
                'empresa': anuncio.empresa,
                'registro': anuncio.registro,
                'sucursal': anuncio.sucursal,
                'liquidacion': anuncio.liquidacion,
                'datos registrales': anuncio.datos_registrales,
                'actos': [],
                'num_actos': 0
            }
            for acto in anuncio.actos:
                acto_dict = {acto.name: acto.value}
                doc['anuncios'][anuncio.id]['num_actos'] += 1
                doc['anuncios'][anuncio.id]['actos'].append(acto_dict)
            num_anuncios += 1

        doc['num_anuncios'] = num_anuncios

        # For compatibility with other parsers
        doc['raw_version'] = RAW_FILE_VERSION
        doc['version'] = FILE_VERSION

        # Note that it requires Internet connection the first time
        if set_url:
            doc['url'] = self.url

        logger.debug(doc)
        return doc

    def to_json(self, path=None, overwrite=True, pretty=True,
                include_url=True):
        """Genera BORME-JSON a partir del archivo PDF

        Nota: Requiere conexión a Internet si include_url=True
        path: directorio o archivo
        overwrite: Sobreescribe el archivo si ya existe
        pretty: Genera el BORME-JSON con indentación para que sea más legible
        include_url: Incluir la URL para descargar el BORME de su fuente
                     oficial posteriormente.
        """
        def set_default(obj):
            """ serialize Python sets as lists
                http://stackoverflow.com/a/22281062
            """
            if isinstance(obj, set):
                return sorted(obj)
            elif isinstance(obj, Provincia):
                return str(obj)
            raise TypeError(type(obj))

        if path is None:
            path = re.sub('(\.pdf)$', '.json', os.path.basename(self.filename))
        if os.path.isfile(path) and not overwrite:
            return False
        if os.path.isdir(path):
            path = os.path.join(path, self.cve + '.json')

        doc = self._to_dict(include_url)
        indent = 2 if pretty else None
        with open(path, 'w') as fp:
            json.dump(doc, fp, default=set_default, indent=indent,
                      sort_keys=True)
        return path

    @classmethod
    def from_json(self, filename):
        """Crea una instancia Borme a partir de un BORME-JSON.

        El parámetro filename puede ser la ruta a un archivo o un objeto file
        de un fichero JSON ya abierto.
        """

        if isinstance(filename, io.IOBase):
            d = json.loads(filename.read())
            filename = filename.name
        else:
            with open(filename) as fp:
                d = json.load(fp)

        if d["version"] < FILE_VERSION:
            logger.warning(
                "This JSON was generated with an older version of bormeparser")
            logger.warning(
                "Current version is {0}, file version is {1}.".format(
                    FILE_VERSION, d["version"]))
        cve = d['cve']
        date = datetime.datetime.strptime(d['date'], '%Y-%m-%d').date()
        seccion = d['seccion']  # TODO: SECCION.from_borme()
        provincia = PROVINCIA.from_title(d['provincia'].upper())
        num = d['num']
        url = d.get('url')  # No obligatorio
        bormeanuncios = []
        anuncios = sorted(d['anuncios'].items(), key=lambda t: t[0])
        for id_anuncio, data in anuncios:
            extra = {
                "liquidacion": data["liquidacion"],
                "sucursal": data["sucursal"],
                "registro": data["registro"]
            }
            a = BormeAnuncio(int(id_anuncio), data['empresa'], data['actos'],
                             extra, data['datos registrales'])
            bormeanuncios.append(a)
        borme = Borme(date, seccion, provincia, num, cve, bormeanuncios,
                      filename)
        borme._url = url
        return borme

    def __lt__(self, other):
        return self.anuncios_rango[1] < other.anuncios_rango[0]

    def __repr__(self):
        return "<Borme({}) seccion:{} provincia:{}>".format(
                    self.date, self.seccion, self.provincia)
