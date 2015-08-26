#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from PyPDF2 import PdfFileReader
from collections import OrderedDict

from bormeparser.regex import regex_cargos, regex_empresa, regex_declaracion, regex_noarg, REGEX_TEXT, REGEX_BORME_NUM, REGEX_BORME_CVE
from bormeparser.acto import ACTO

logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.WARN)

DATA = OrderedDict()
for key in ('borme_fecha', 'borme_num', 'borme_seccion', 'borme_subseccion', 'borme_provincia', 'borme_cve'):
    DATA[key] = None


def clean_data(data):
    return data.replace('\(', '(').replace('\)', ')').replace('  ', ' ').strip()


def parse_file(filename):
    cabecera = False
    texto = False
    data = ""
    actos = {}
    nombreacto = None
    anuncio_id = None
    empresa = None
    fecha = False
    numero = False
    seccion = False
    subseccion = False
    provincia = False
    cve = False

    reader = PdfFileReader(open(filename, 'rb'))
    for n in range(0, reader.getNumPages()):
        content = reader.getPage(n).getContents().getData()
        logger.debug('---- BEGIN OF PAGE ----')
        
        # Python 3
        if isinstance(content, bytes):
            content = content.decode('unicode_escape')
        #logger.debug(content)

        for line in content.split('\n'):
            logger.debug('### LINE: %s' % line)
            if line.startswith('/Cabecera_acto'):
                logger.debug('START: cabecera')
                cabecera = True
                data = ""
                actos = {}
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
                    data = clean_data(data)
                    anuncio_id, empresa = regex_empresa(data)
                    logger.debug('  anuncio_id: %s' % anuncio_id)
                    logger.debug('  empresa: %s' % empresa)
                    data = ""
                if texto:
                    logger.debug('END: texto')
                    texto = False
                    logger.debug('  nombreacto: %s' % nombreacto)
                    logger.debug('  data: %s' % data)

                    if nombreacto:
                        data = clean_data(data)
                        actos[nombreacto] = data
                        logger.debug('  nombreacto: %s' % nombreacto)
                        logger.debug('  data: %s' % data)
                        DATA[anuncio_id] = {'Empresa': empresa, 'Actos': actos}
                        nombreacto = None
                continue

            if not any([texto, cabecera, fecha, numero, seccion, subseccion, provincia, cve]):
                continue

            if line == '/F1 8 Tf':
                # Font 1: bold
                if nombreacto:
                    logger.debug('  nombreacto: %s' % nombreacto)
                    data = clean_data(data)
                    logger.debug('  data: %s' % data)
                    if nombreacto in ACTO.CARGOS_KEYWORDS:
                        data = regex_cargos(data)
                    logger.debug('  data_2: %s' % data)
                    actos[nombreacto] = data
                    data = ""
                    nombreacto = None
                logger.debug('START: font bold')
                continue

            if line == '/F2 8 Tf':
                # Font 2: normal
                # FIXME: (223238) Sociedad unipersonal. Cambio de identidad del socio único: MORENO NAVAS CARLOS.
                # HACK

                # Capturar lo necesario y dejar el resto en nombramientos, clean_data doblemente.
                nombreacto = clean_data(data)[:-1]
                if 'Declaración de unipersonalidad.' in nombreacto:
                    socio_unico, nombreacto = regex_declaracion(nombreacto)
                    actos['Declaración de unipersonalidad'] = {'Socio Único': {socio_unico}}
                    logger.debug('  nombreacto2 Declaración de unipersonalidad')
                    logger.debug('  data: %s' % socio_unico)
                elif any(kw+'.' in nombreacto for kw in ACTO.NOARG_KEYWORDS):
                    acto_noarg, nombreacto = regex_noarg(nombreacto)
                    actos[acto_noarg] = True
                    logger.debug('  acto_noarg2: %s' % acto_noarg)
                    logger.debug('  data: %s' % data)

                logger.debug('  nombreacto2: %s' % nombreacto)
                logger.debug('  data: %s' % data)
                data = ""
                logger.debug('  data_1: %s' % data)
                logger.debug('START: font normal')
                continue

            m = REGEX_TEXT.match(line)
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
                #logger.debug(m.group(1))
                data += ' ' + m.group(1)
                #logger.debug('MORE DATA')
                logger.debug('TOTAL DATA: %s' % data)

        logger.debug('---- END OF PAGE ----')

    return DATA