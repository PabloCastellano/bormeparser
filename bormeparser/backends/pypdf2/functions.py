#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileReader
from bormeparser.regex import regex_cargos, REGEX_EMPRESA, REGEX_TEXT
from bormeparser.acto import ACTO

ACTOS = {}


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

    # Python 3
    if isinstance(content, bytes):
        content = content.decode('unicode_escape')
    #print(content)

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

        if line == 'BT':
            # Begin text object
            continue

        if line == 'ET':
            # End text object
            if cabecera:
                cabecera = False
                data = clean_data(data)
                m = REGEX_EMPRESA.match(data)
                acto_id = int(m.group(1))
                empresa = m.group(2)
            if texto:
                texto = False
                data = clean_data(data)
                actos[nombreacto] = data
                ACTOS[acto_id] = {'Empresa': empresa, 'Actos': actos}
            continue

        if not texto and not cabecera:
            continue

        if line == '/F1 8 Tf':
            # Font 1: bold
            data = clean_data(data)
            if nombreacto in ACTO.CARGOS_KEYWORDS:
                data = regex_cargos(data)
            actos[nombreacto] = data
            data = ""
            continue

        if line == '/F2 8 Tf':
            # Font 2: normal

            # Declaración de unipersonalidad. Socio único: FUENTES GARCIA JUAN CARLOS. Nombramientos
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
            #print(m.group(1))
            data += ' ' + m.group(1)


def parse_file(filename):
    reader = PdfFileReader(open(filename, 'rb'))
    for n in range(0, reader.getNumPages()):
        content = reader.getPage(n).getContents().getData()
        parse_content(content)
    return ACTOS
