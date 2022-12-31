#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# bormeparser.backends.pypdf2.parser.py -
# Copyright (C) 2015-2022 Pablo Castellano <pablo@anche.no>
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

#from __future__ import absolute_import
from bormeparser.backends.base import BormeAParserBackend
import logging

from PyPDF2 import PdfFileReader

from bormeparser.regex import regex_cargos, regex_empresa, regex_argcolon, regex_noarg, is_acto_cargo, is_acto_bold,\
                              regex_bold_acto, REGEX_ARGCOLON, REGEX_NOARG, REGEX_PDF_TEXT, REGEX_BORME_NUM, REGEX_BORME_CVE,\
                              is_acto_bold_mix

from ..defaults import OPTIONS

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)

actos = []


class PyPDF2Parser(BormeAParserBackend):
    """
    Parse using PyPDF2
    """
    def __init__(self, filename, log_level=logging.WARN):
        super(PyPDF2Parser, self).__init__(filename)
        logger.setLevel(log_level)
        self.actos = []
        self.sanitize = OPTIONS['SANITIZE_COMPANY_NAME']

    def _parse(self):
        cabecera = False
        changing_page = False
        cve = False
        data = ""
        fecha = False
        last_font = 0
        nombreacto = None
        numero = False
        provincia = False
        seccion = False
        subseccion = False
        texto = False
        anuncio_id = None
        empresa = None
        extra = None

        DATA = {
            'borme_fecha': None,
            'borme_num': None,
            'borme_seccion': None,
            'borme_subseccion': None,
            'borme_provincia': None,
            'borme_cve': None
        }
        self.actos = []

        fp = open(self.filename, 'rb')
        reader = PdfFileReader(fp)
        for n in range(0, reader.getNumPages()):
            content = reader.getPage(n).getContents().getData()
            logger.debug('---- BEGIN OF PAGE ----')

            # Python 3
            if isinstance(content, bytes):
                content = content.decode('unicode_escape')

            for line in content.split('\n'):
                logger.debug('### LINE: %s' % line)
                if line.startswith('/Cabecera_acto'):
                    logger.debug('START: cabecera')
                    cabecera = True

                    if changing_page:
                        changing_page = False

                    logger.debug('  BT nombreacto: %s' % nombreacto)
                    logger.debug('  BT data: %s' % data)

                    if nombreacto:
                        self._parse_acto(nombreacto, data, prefix='BT')
                        nombreacto = None
                        DATA[anuncio_id] = {
                            'Empresa': empresa,
                            'Extra': extra,
                            'Actos': self.actos
                        }

                    data = ""
                    self.actos = []
                    continue

                if line.startswith('/Texto_acto'):
                    logger.debug('START: texto')
                    logger.debug('  nombreacto: %s' % nombreacto)
                    logger.debug('  data: %s' % data)
                    texto = True
                    continue

                if line.startswith('/Fecha'):
                    if not DATA['borme_fecha']:
                        logger.debug('START: fecha')
                        fecha = True
                    continue

                if line.startswith('/Numero_BORME'):
                    if not DATA['borme_num']:
                        logger.debug('START: numero')
                        numero = True
                    continue

                if line.startswith('/Seccion'):
                    if not DATA['borme_seccion']:
                        logger.debug('START: seccion')
                        seccion = True
                    continue

                if line.startswith('/Subseccion'):
                    if not DATA['borme_subseccion']:
                        logger.debug('START: subseccion')
                        subseccion = True
                    continue

                if line.startswith('/Provincia'):
                    if not DATA['borme_provincia']:
                        logger.debug('START: provincia')
                        provincia = True
                    continue

                if line.startswith('/Codigo_verificacion'):
                    if not DATA['borme_cve']:
                        logger.debug('START: cve')
                        cve = True
                    continue

                if line == 'BT':
                    # Begin text object
                    continue

                if line == 'ET':
                    # End text object
                    if cabecera:
                        logger.debug('END: cabecera')
                        cabecera = False
                        data = self._clean_data(data)
                        anuncio_id, empresa, extra = regex_empresa(data, sanitize=self.sanitize)
                        logger.debug('  anuncio_id: %s' % anuncio_id)
                        logger.debug('  empresa: %s' % empresa)
                        logger.debug('  extra: {}'.format(extra))
                        data = ""
                    if texto:
                        logger.debug('END: texto')
                        texto = False
                        logger.debug('  nombreacto: %s' % nombreacto)
                        logger.debug('  data: %s' % data)
                    continue

                if not any([texto, cabecera, fecha, numero, seccion, subseccion, provincia, cve]):
                    continue

                if line == '/F1 8 Tf':
                    # Font 1: bold
                    logger.debug('START: font bold. %s %s' % (changing_page, last_font))
                    if changing_page:
                        # FIXME: Estoy suponiendo que una cabecera no se queda partida entre dos paginas
                        if nombreacto and last_font == 2:
                            self._parse_acto(nombreacto, data, prefix='F1')
                            nombreacto = None
                            data = ""
                        changing_page = False
                    else:
                        if nombreacto:
                            self._parse_acto(nombreacto, data, prefix='F1')
                            nombreacto = None
                            data = ""

                    logger.debug('  nombreacto: %s' % nombreacto)
                    logger.debug('  data: %s' % data)
                    last_font = 1
                    continue

                if line == '/F2 8 Tf':
                    # Font 2: normal
                    logger.debug('START: font normal. %s %s' % (changing_page, last_font))
                    logger.debug('  nombreacto2: %s' % nombreacto)
                    logger.debug('  data: %s' % data)

                    if changing_page:
                        changing_page = False
                        if not nombreacto:
                            nombreacto = self._clean_data(data)[:-1]
                        if last_font != 1:
                            last_font = 2
                            continue
                    nombreacto = self._clean_data(data)[:-1]

                    while True:
                        end, nombreacto = self._parse_acto_bold(nombreacto, data)
                        if end:
                            break

                    if is_acto_bold_mix(nombreacto):
                        nombreacto = "Escisión total"
                        data = "Sociedades beneficiarias de la escisión:"
                    else:
                        data = ""
                    logger.debug('  data_1: %s' % data)
                    last_font = 2
                    continue

                m = REGEX_PDF_TEXT.match(line)
                if m:
                    if fecha:
                        DATA['borme_fecha'] = m.group(1)
                        fecha = False
                        logger.debug('fecha: %s' % DATA['borme_fecha'])
                    if numero:
                        text = m.group(1)
                        DATA['borme_num'] = int(REGEX_BORME_NUM.match(text).group(1))
                        numero = False
                        logger.debug('num: %d' % DATA['borme_num'])
                    if seccion:
                        DATA['borme_seccion'] = m.group(1)
                        seccion = False
                        logger.debug('seccion: %s' % DATA['borme_seccion'])
                    if subseccion:
                        DATA['borme_subseccion'] = m.group(1)
                        subseccion = False
                        logger.debug('subseccion: %s' % DATA['borme_subseccion'])
                    if provincia:
                        DATA['borme_provincia'] = m.group(1)
                        provincia = False
                        logger.debug('provincia: %s' % DATA['borme_provincia'])
                    if cve:
                        text = m.group(1)
                        DATA['borme_cve'] = REGEX_BORME_CVE.match(text).group(1)
                        cve = False
                        logger.debug('cve: %s' % DATA['borme_cve'])
                    data += ' ' + m.group(1)
                    logger.debug('TOTAL DATA: %s' % data)

            logger.debug('---- END OF PAGE ----')
            changing_page = True

        if nombreacto:
            self._parse_acto(nombreacto, data, prefix='END')
            if not empresa:
                logger.warning(msg='No se encontró la empresa en el fichero %s' % self.filename)
            if not extra:
                logger.warning(msg='No se encontró el "extra" en el fichero %s' % self.filename)
            if not anuncio_id:
                logger.warning(msg='No se encontró el anuncio_id en el fichero %s' % self.filename)
            DATA[anuncio_id] = {
                'Empresa': empresa,
                'Extra': extra,
                'Actos': self.actos
            }

        fp.close()
        return DATA

    def _clean_data(self, data):
        """ Unscape parenthesis and removes double spaces """
        return data.replace('\(', '(').replace('\)', ')').replace('  ', ' ').strip()

    def _parse_acto(self, nombreacto, data, prefix=''):
        data = self._clean_data(data)
        if is_acto_cargo(nombreacto):
            cargos = regex_cargos(data, sanitize=self.sanitize)
            if not cargos:
                logger.warning(f'No se encontraron cargos en la cadena: {data}\n\tdel fichero {self.filename}')
            data = cargos

        logger.debug('  %s nombreactoW: %s' % (prefix, nombreacto))
        logger.debug('  %s dataW: %s' % (prefix, data))
        self.actos.append({nombreacto: data})

    def _parse_acto_bold(self, nombreacto, data):
        end = False
        if not nombreacto:
            logger.debug('No hay nombreacto')
            return end, nombreacto

        if is_acto_bold_mix(nombreacto):
            end = True
        elif is_acto_bold(nombreacto):
            acto_colon, arg_colon, nombreacto = regex_bold_acto(nombreacto)
            if not nombreacto:
                logger.warning(msg='No se encontró el nombre del acto en el fichero %s' % self.filename)
            self.actos.append({acto_colon: arg_colon})

            logger.debug('  F2 nombreactoW: %s -- %s' % (acto_colon, arg_colon))
            logger.debug('  nombreacto: %s' % nombreacto)
            logger.debug('  data: %s' % data)
        elif REGEX_ARGCOLON.match(nombreacto):
            acto_colon, arg_colon, nombreacto = regex_argcolon(nombreacto)
            # FIXME: check
            self.actos.append({acto_colon: arg_colon})

            logger.debug('  F2 nombreactoW: %s -- %s' % (acto_colon, arg_colon))
            logger.debug('  nombreacto: %s' % nombreacto)
            logger.debug('  data: %s' % data)
        elif REGEX_NOARG.match(nombreacto):
            acto_noarg, nombreacto = regex_noarg(nombreacto)
            self.actos.append({acto_noarg: None})
            logger.debug('  F2 acto_noargW: %s -- True' % acto_noarg)
            logger.debug('  nombreacto: %s' % nombreacto)
            logger.debug('  data: %s' % data)
        else:
            end = True
        return end, nombreacto


if __name__ == '__main__':
    import pprint
    actos = PyPDF2Parser('examples/BORME-A-2015-27-10.pdf').parse()
    pprint.pprint(actos, width=160)
