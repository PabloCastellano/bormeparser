#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from PyPDF2 import PdfFileReader

from bormeparser.regex import regex_cargos, regex_empresa, REGEX_TEXT, REGEX_BORME_NUM, REGEX_BORME_CVE
from bormeparser.acto import ACTO

logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.WARN)

DATA = {'borme_fecha': None, 'borme_num': None, 'borme_seccion': None, 'borme_subseccion': None,
        'borme_provincia': None, 'borme_cve': None}


def clean_data(data):
    return data.replace('\(', '(').replace('\)', ')').replace('  ', ' ').strip()


def parse_content(content):
    cabecera = False
    texto = False
    data = ""
    actos = {}
    nombreacto = None
    acto_id = None
    empresa = None
    fecha = False
    numero = False
    seccion = False
    subseccion = False
    provincia = False
    cve = False

    # Python 3
    if isinstance(content, bytes):
        content = content.decode('unicode_escape')
    logger.debug(content)

    for line in content.split('\n'):
        if line.startswith('/Cabecera_acto'):
            cabecera = True
            data = ""
            actos = {}
            continue

        if line.startswith('/Texto_acto'):
            texto = True
            data = ""
            continue

        if line.startswith('/Fecha'):
            if not DATA['borme_fecha']:
                fecha = True
            continue

        if line.startswith('/Numero_BORME'):
            if not DATA['borme_num']:
                numero = True
            continue

        if line.startswith('/Seccion'):
            if not DATA['borme_seccion']:
                seccion = True
            continue

        if line.startswith('/Subseccion'):
            if not DATA['borme_subseccion']:
                subseccion = True
            continue

        if line.startswith('/Provincia'):
            if not DATA['borme_provincia']:
                provincia = True
            continue

        if line.startswith('/Codigo_verificacion'):
            if not DATA['borme_cve']:
                cve = True
            continue

        if line == 'BT':
            # Begin text object
            continue

        if line == 'ET':
            # End text object
            if cabecera:
                cabecera = False
                data = clean_data(data)
                acto_id, empresa = regex_empresa(data)
            if texto:
                texto = False
                data = clean_data(data)
                actos[nombreacto] = data
                DATA[acto_id] = {'Empresa': empresa, 'Actos': actos}
            continue

        if not any([texto, cabecera, fecha, numero, seccion, subseccion, provincia, cve]):
            continue

        if line == '/F1 8 Tf':
            # Font 1: bold
            if nombreacto:
                data = clean_data(data)
                if nombreacto in ACTO.CARGOS_KEYWORDS:
                    data = regex_cargos(data)
                actos[nombreacto] = data
            data = ""
            continue

        if line == '/F2 8 Tf':
            # Font 2: normal

            # FIXME: Declaración de unipersonalidad. Socio único: GARCIA FUENTES JUAN CARLOS. Nombramientos
            """
            if nombreacto and 'Declaración de unipersonalidad' in nombreacto:
                nombreacto = clean_data(data)[:-1]
                f = nombreacto.rfind('.')
                data = nombreacto[f+1:]
                nombreacto = nombreacto[:f+1]
                actos[nombreacto] = 'X'
            """
            nombreacto = clean_data(data)[:-1]
            data = ""
            continue

        m = REGEX_TEXT.match(line)
        if m:
            if fecha:
                DATA['borme_fecha'] = m.group(1)
                fecha = False
            if numero:
                text = m.group(1)
                DATA['borme_num'] = int(REGEX_BORME_NUM.match(text).group(1))
                numero = False
            if seccion:
                DATA['borme_seccion'] = m.group(1)
                seccion = False
            if subseccion:
                DATA['borme_subseccion'] = m.group(1)
                subseccion = False
            if provincia:
                DATA['borme_provincia'] = m.group(1)
                provincia = False
            if cve:
                text = m.group(1)
                DATA['borme_cve'] = REGEX_BORME_CVE.match(text).group(1)
                cve = False
            logger.debug(m.group(1))
            data += ' ' + m.group(1)


def parse_file(filename):
    reader = PdfFileReader(open(filename, 'rb'))
    for n in range(0, reader.getNumPages()):
        content = reader.getPage(n).getContents().getData()
        parse_content(content)
    return DATA
