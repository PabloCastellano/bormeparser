#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from PyPDF2 import PdfFileReader
from collections import OrderedDict

from bormeparser.regex import regex_cargos, regex_empresa, regex_declaracion, REGEX_TEXT, REGEX_BORME_NUM, REGEX_BORME_CVE
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
                texto = True
                data = ""
                continue

            if line.startswith('/Fecha'):
                logger.debug('START: fecha')
                if not DATA['borme_fecha']:
                    fecha = True
                continue

            if line.startswith('/Numero_BORME'):
                logger.debug('START: numero')
                if not DATA['borme_num']:
                    numero = True
                continue

            if line.startswith('/Seccion'):
                logger.debug('START: seccion')
                if not DATA['borme_seccion']:
                    seccion = True
                continue

            if line.startswith('/Subseccion'):
                logger.debug('START: subseccion')
                if not DATA['borme_subseccion']:
                    subseccion = True
                continue

            if line.startswith('/Provincia'):
                logger.debug('START: provincia')
                if not DATA['borme_provincia']:
                    provincia = True
                continue

            if line.startswith('/Codigo_verificacion'):
                logger.debug('START: cve')
                if not DATA['borme_cve']:
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
                if texto:
                    logger.debug('END: texto')
                    texto = False

                    # Check Declaracion de unip... in data
                    if 'Declaración de unipersonalidad' in data:
                        socio_unico, nombreacto = regex_declaracion(data)
                        actos['Declaración de unipersonalidad'] = socio_unico
                        logger.debug('  nombreacto1: %s' % nombreacto)
                        logger.debug('  data: %s' % data)

                    if nombreacto:
                        data = clean_data(data)
                        actos[nombreacto] = data
                        logger.debug('  nombreacto1: %s' % nombreacto)
                        logger.debug('  data: %s' % data)
                    DATA[anuncio_id] = {'Empresa': empresa, 'Actos': actos}
                    nombreacto = None
                continue

            if not any([texto, cabecera, fecha, numero, seccion, subseccion, provincia, cve]):
                continue

            if line == '/F1 8 Tf':
                # Font 1: bold
                logger.debug('START: font bold')
                if nombreacto:
                    logger.debug('  nombreacto: %s' % nombreacto)
                    logger.debug('  data: %s' % data)
                    data = clean_data(data)
                    logger.debug('  data_1: %s' % data)
                    if nombreacto in ACTO.CARGOS_KEYWORDS:
                        data = regex_cargos(data)
                    logger.debug('  data_2: %s' % data)
                    actos[nombreacto] = data
                    data = ""
                continue

            if line == '/F2 8 Tf':
                # Font 2: normal
                logger.debug('START: font normal')
                # FIXME: Declaración de unipersonalidad. Socio único: GARCIA FUENTES JUAN CARLOS. Nombramientos
                # FIXME: (223969) Extinción. Datos registrales. T 4889, L 3797, F 13, S 8, H MA109474, I/A 2 (21.05.15).
                # FIXME: (223238) Sociedad unipersonal. Cambio de identidad del socio único: MORENO NAVAS CARLOS.
                # HACK
                """
                if nombreacto and 'Declaración de unipersonalidad' in nombreacto:
                    nombreacto = clean_data(data)[:-1]
                    f = nombreacto.rfind('.')
                    data = nombreacto[f+1:]
                    nombreacto = nombreacto[:f+1]
                    actos[nombreacto] = 'X'

                if 'Extinción' in nombreacto or 'Declaración de unipersonalidad' in nombreacto:
                    pass

                if nombreacto.startswith('Declaración de unipersonalidad'):
                    actos['Declaración de unipersonalidad'] = nombreacto.rsplit('.', 1)[0][32:]
                    nombreacto = clean_data(nombreacto.rsplit('.', 1)[1])
                """

                """
                if 'Declaración de unipersonalidad' in nombreacto:
                    socio_unico, acto = regex_declaracion(nombreacto)
                    actos['Declaración de unipersonalidad'] = socio_unico
                    nombreacto = acto
                """

                # Capturar lo necesario y dejar el resto en nombramientos, clean_data doblemente.
                nombreacto = clean_data(data)[:-1]
                logger.debug('  nombreacto2: %s' % nombreacto)
                logger.debug('  data: %s' % data)
                data = ""
                logger.debug('  data_1: %s' % data)
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

        # final de pagina, guardar lo que haya en data
        logger.debug('---- END OF PAGE ----')
        """
        import pdb
        pdb.set_trace()
        """
    return DATA