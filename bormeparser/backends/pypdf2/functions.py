#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from PyPDF2 import PdfFileReader
from collections import OrderedDict

from bormeparser.regex import regex_cargos, regex_empresa, regex_argcolon, regex_noarg, is_acto_cargo, is_acto_rare,\
                              regex_decl_unip, REGEX_ARGCOLON, REGEX_NOARG, REGEX_PDF_TEXT, REGEX_BORME_NUM, REGEX_BORME_CVE,\
                              is_acto_escision, regex_escision, regex_fusion, is_acto_fusion

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)

actos = OrderedDict()


def clean_data(data):
    """ Unscape parenthesis and removes double spaces """
    return data.replace('\(', '(').replace('\)', ')').replace('  ', ' ').strip()


def parse_acto(nombreacto, data, prefix=''):
    data = clean_data(data)
    if is_acto_cargo(nombreacto):
        cargos = regex_cargos(data)
        if not cargos:
            logger.warning('No se encontraron cargos en la cadena: %s' % data)
        data = cargos
    elif is_acto_escision(nombreacto):
        nombreacto, data = regex_escision(nombreacto, data)
    elif is_acto_fusion(nombreacto):
        data = regex_fusion(data)

    logger.debug('  %s nombreactoW: %s' % (prefix, nombreacto))
    logger.debug('  %s dataW: %s' % (prefix, data))
    actos[nombreacto] = data


def parse_acto_bold(nombreacto, data):
    global actos
    end = False

    if is_acto_rare(nombreacto):
        # TODO: u'Acuerdo de ampliación de capital social sin ejecutar. Importe del acuerdo'
        if nombreacto.startswith(u'Declaración de unipersonalidad'):
            acto_colon, arg_colon, nombreacto = regex_decl_unip(nombreacto)
            actos[acto_colon] = True
        else:
            acto_colon, arg_colon, nombreacto = regex_decl_unip(nombreacto)
            actos[acto_colon] = arg_colon

        logger.debug('  F2 nombreactoW: %s -- %s' % (acto_colon, arg_colon))
        logger.debug('  nombreacto: %s' % nombreacto)
        logger.debug('  data: %s' % data)
    elif REGEX_ARGCOLON.match(nombreacto):
        acto_colon, arg_colon, nombreacto = regex_argcolon(nombreacto)
        # FIXME: check
        actos[acto_colon] = arg_colon

        logger.debug('  F2 nombreactoW: %s -- %s' % (acto_colon, arg_colon))
        logger.debug('  nombreacto: %s' % nombreacto)
        logger.debug('  data: %s' % data)
    elif REGEX_NOARG.match(nombreacto):
        acto_noarg, nombreacto = regex_noarg(nombreacto)
        actos[acto_noarg] = True
        logger.debug('  F2 acto_noargW: %s -- True' % acto_noarg)
        logger.debug('  nombreacto: %s' % nombreacto)
        logger.debug('  data: %s' % data)
    else:
        end = True
    return end, nombreacto


def parse_file(filename):
    global actos
    anuncio_id = None
    cabecera = False
    changing_page = False
    cve = False
    data = ""
    empresa = None
    fecha = False
    last_font = 0
    nombreacto = None
    numero = False
    provincia = False
    seccion = False
    subseccion = False
    texto = False

    DATA = OrderedDict()
    for key in ('borme_fecha', 'borme_num', 'borme_seccion', 'borme_subseccion', 'borme_provincia', 'borme_cve'):
        DATA[key] = None
    actos.clear()

    reader = PdfFileReader(open(filename, 'rb'))
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
                    parse_acto(nombreacto, data, prefix='BT')
                    nombreacto = None
                    DATA[anuncio_id] = {'Empresa': empresa, 'Actos': actos}

                data = ""
                actos = OrderedDict()
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
                continue

            if not any([texto, cabecera, fecha, numero, seccion, subseccion, provincia, cve]):
                continue

            if line == '/F1 8 Tf':
                # Font 1: bold
                logger.debug('START: font bold. %s %s' % (changing_page, last_font))
                if changing_page:
                    # FIXME: Estoy suponiendo que una cabecera no se queda partida entre dos paginas
                    if nombreacto and last_font == 2:
                        parse_acto(nombreacto, data, prefix='F1')
                        nombreacto = None
                        data = ""
                    changing_page = False
                else:
                    if nombreacto:
                        parse_acto(nombreacto, data, prefix='F1')
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
                        nombreacto = clean_data(data)[:-1]
                    if last_font != 1:
                        last_font = 2
                        continue
                nombreacto = clean_data(data)[:-1]

                while True:
                    end, nombreacto = parse_acto_bold(nombreacto, data)
                    if end:
                        break

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
        parse_acto(nombreacto, data, prefix='END')
        DATA[anuncio_id] = {'Empresa': empresa, 'Actos': actos}

    return DATA
