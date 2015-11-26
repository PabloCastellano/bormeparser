#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from bormeparser.acto import ACTO
from bormeparser.cargo import CARGO

esc_arg_keywords = [x.replace('.', '\.') for x in ACTO.ALL_KEYWORDS]
esc_colon_keywords = [x.replace('.', '\.') for x in ACTO.COLON_KEYWORDS]
esc_rare_keywords = [x.replace('.', '\.') for x in ACTO.RARE_KEYWORDS]
esc_noarg_keywords = [x.replace('.', '\.').replace('(', '\(').replace(')', '\)') for x in ACTO.NOARG_KEYWORDS]
esc_ending_keywords = [x.replace('.', '\.') for x in ACTO.ENDING_KEYWORDS]

esc_cargos_keywords = [x.replace('.', '\.') for x in CARGO.KEYWORDS]

# -- ACTOS --
# OR de las palabras clave con argumentos
RE_ARG_KEYWORDS = '(%s)' % '|'.join(esc_arg_keywords)
RE_ALL_KEYWORDS = '(%s|%s|%s|%s)' % ('|'.join(esc_arg_keywords), '|'.join(esc_colon_keywords),
                                     '|'.join(esc_noarg_keywords), esc_ending_keywords[0])
# OR de las palabras clave, "non grouping"
RE_ALL_KEYWORDS_NG = '(?:%s|%s|%s|%s)' % ('|'.join(esc_arg_keywords), '|'.join(esc_colon_keywords),
                                          '|'.join(esc_noarg_keywords), esc_ending_keywords[0])
# OR de las palabras clave sin argumentos
RE_NOARG_KEYWORDS = '(%s)' % '|'.join(esc_noarg_keywords)
# OR de las palabras clave con argumentos seguidas por :
RE_COLON_KEYWORDS = '(%s)' % '|'.join(esc_colon_keywords)
RE_RARE_KEYWORDS = '(%s)' % '|'.join(esc_rare_keywords)
RE_ENDING_KEYWORD = '(%s)' % esc_ending_keywords[0]

# -- CARGOS --
# OR de las palabras clave
RE_CARGOS_KEYWORDS = '(%s)' % '|'.join(esc_cargos_keywords)
# RE para capturar el cargo y los nombres
RE_CARGOS_MATCH = RE_CARGOS_KEYWORDS + ":\s(.*?)(?:\.$|\. |\s*$)"

"""
DEPRECATED
REGEX1 = re.compile('^(\d+) - (.*?)\.\s*' + RE_ALL_KEYWORDS_NG)
# Captura cada palabra clave con sus argumentos
REGEX2 = re.compile('(?=' + RE_ARG_KEYWORDS + '\.\s+(.*?)\.\s*' + RE_ALL_KEYWORDS_NG + ')')
REGEX3 = re.compile(RE_COLON_KEYWORDS + ':\s+(.*?)\.\s*' + RE_ALL_KEYWORDS_NG)
REGEX4 = re.compile(RE_ENDING_KEYWORD + '\.\s+(.*)\.\s*')
REGEX5 = re.compile(RE_NOARG_KEYWORDS + '\.')
"""

REGEX_NOARG = re.compile(RE_NOARG_KEYWORDS + '\.\s*(.*)', re.UNICODE)
REGEX_ARGCOLON = re.compile(RE_COLON_KEYWORDS + ': (.*?)(?:\.\s+)(.*)', re.UNICODE)
REGEX_RARE = re.compile(RE_RARE_KEYWORDS + ': (.*?)\.\s*' + RE_ARG_KEYWORDS + '(.*)', re.UNICODE)

REGEX_EMPRESA = re.compile('^(\d+)\s+-\s+(.*?)(?:\.$|$)')
REGEX_PDF_TEXT = re.compile('^\((.*)\)Tj$')
REGEX_BORME_NUM = re.compile(u'^Núm\. (\d+)', re.UNICODE)
REGEX_BORME_FECHA = re.compile('^\w+ (\d+) de (\w+) de (\d+)')
REGEX_BORME_CVE = re.compile('^cve: (.*)$')

MESES = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6, 'julio': 7,
         'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12}


# https://es.wikipedia.org/wiki/Anexo:Tipos_de_sociedad_mercantil_en_Espa%C3%B1a
SOCIEDADES = {'AIE': 'Agrupación de Interés Económico',
              'AEIE': 'Agrupación Europea de Interés Económico',
              'COOP': 'Cooperativa',
              'FP': 'Fondo de Pensiones',
              'SA': 'Sociedad Anónima',
              'SAL': 'Sociedad Anónima Laboral',
              'SAP': 'Sociedad Anónima P?',
              'SAU': 'Sociedad Anónima Unipersonal',
              'SCP': 'Sociedad Civil Profesional',
              'SL': 'Sociedad Limitada',
              'SLL': 'Sociedad Limitada Laboral',
              'SLNE': 'Sociedad Limitada Nueva Empresa',
              'SLP': 'Sociedad Limitada Profesional',
              'SLU': 'Sociedad Limitada Unipersonal',
              'SRL': 'Sociedad de Responsabilidad Limitada',
              'SRLL': 'Sociedad de Responsabilidad Limitada Laboral',
              'SRLP': 'Sociedad de Responsabilidad Limitada Profesional',
              }
# SOCIEDAD COOPERATIVA DE CREDITO
# FONDOS DE PENSIONES


def is_acto_cargo_entrante(data):
    """ Comprueba si es un acto que aporta nuevos cargos """

    if not is_acto_cargo(data) and not is_acto_rare_cargo(data):
        raise ValueError('No es un acto con cargos: %s' % data)
    return data in ['Reelecciones', 'Nombramientos']


def is_acto_cargo(data):
    """ Comprueba si es un acto que tiene como parámetro una lista de cargos """
    actos = ['Revocaciones', 'Reelecciones', 'Cancelaciones de oficio de nombramientos', 'Nombramientos', 'Ceses/Dimisiones',
             u'Emisión de obligaciones', u'Modificación de poderes']
    return data in actos


def is_acto_noarg(data):
    """ Comprueba si es un acto que no tiene parametros """
    return data in ACTO.NOARG_KEYWORDS


def is_acto_rare_cargo(data):
    """ Como is_acto_cargo pero se parsean de forma distinta """
    actos = (u'Declaración de unipersonalidad', u'Cambio de identidad del socio único',
             u'Escisión parcial', u'Escisión total', u'Fusión por unión')
    return data in actos


def is_acto_rare(data):
    for acto in ACTO.RARE_KEYWORDS:
        if data.startswith(acto):
            return True
    return False


def is_company(data):
    """ Comprueba si es algún tipo de sociedad o por el contrario es una persona física """
    siglas = list(SOCIEDADES.keys())
    siglas = list(map(lambda x: ' %s' % x, siglas))
    return any(data.endswith(s) for s in siglas)


def is_acto_escision(nombreacto):
    return nombreacto in (u'Escisión total. Sociedades beneficiarias de la escisión', u'Escisión parcial')


def is_acto_fusion(nombreacto):
    return nombreacto == u'Fusión por unión'


# HACK
def regex_argcolon(data):
    """ Captura el acto y su argumento y el siguiente acto """
    acto_colon, arg_colon, nombreacto = REGEX_ARGCOLON.match(data).groups()
    return acto_colon, arg_colon, nombreacto


# HACK
def regex_noarg(data):
    """ Captura el acto sin argumento y el siguiente acto """
    nombreacto, siguiente_acto = REGEX_NOARG.match(data).groups()
    return nombreacto, siguiente_acto


def regex_empresa_tipo(data):
    empresa = data
    tipo = ''
    for t in SOCIEDADES.keys():
        if data.endswith(' %s' % t):
            empresa = data[:-len(t) - 1]
            tipo = t
            if empresa.endswith(','):
                empresa = empresa[:-1]
    return empresa, tipo


def regex_empresa(data, sanitize=True):
    """ Captura el número de acto y el nombre de la empresa """
    acto_id, empresa = REGEX_EMPRESA.match(data).groups()
    if sanitize:
        empresa = regex_nombre_empresa(empresa)
    return int(acto_id), empresa


# TODO: Devolver palabras clave como SICAV, SUCURSAL, EN LIQUIDACION
def regex_nombre_empresa(nombre):
    if nombre.endswith(u'(R.M. A CORUÑA)'):
        nombre = nombre[:-15]
    if nombre.endswith('(R.M. PALMA DE MALLORCA)'):
        nombre = nombre[:-24]
    if nombre.endswith('(R.M. PUERTO DE ARRECIFE)'):
        nombre = nombre[:-25]
    if nombre.endswith('(R.M. PUERTO DEL ROSARIO)'):
        nombre = nombre[:-25]
    if nombre.endswith('(R.M. SANTIAGO DE COMPOSTELA)'):
        nombre = nombre[:-29]
    if nombre.endswith('(R.M. SANTA CRUZ DE TENERIFE)'):
        nombre = nombre[:-29]
    if nombre.endswith('(R.M. SANTA CRUZ DE LA PALMA)'):
        nombre = nombre[:-29]
    if nombre.endswith('(R.M. LAS PALMAS)'):
        nombre = nombre[:-17]
    if nombre.endswith('(R.M. EIVISSA)'):
        nombre = nombre[:-14]
    if nombre.endswith('EN LIQUIDACION'):
        nombre = nombre[:-15]
    if nombre.endswith(u'SUCURSAL EN ESPAÑA'):
        nombre = nombre[:-18]
    nombre.rstrip()
    if nombre.endswith(' S.L.'):
        nombre = nombre[:-4] + 'SL'
    if nombre.endswith(' S.L'):
        nombre = nombre[:-3] + 'SL'
    if nombre.endswith(' S L'):
        nombre = nombre[:-3] + 'SL'
    elif nombre.endswith(' SOCIEDAD LIMITADA'):
        nombre = nombre[:-17] + 'SL'
    elif nombre.endswith(' SOCIETAT LIMITADA'):
        nombre = nombre[:-17] + 'SL'
    elif nombre.endswith(' S.A.L'):
        nombre = nombre[:-5] + 'SAL'
    elif nombre.endswith(' SOCIEDAD ANONIMA LABORAL'):
        nombre = nombre[:-24] + 'SAL'
    elif nombre.endswith(' S.A'):
        nombre = nombre[:-3] + 'SA'
    elif nombre.endswith(' SOCIEDAD ANONIMA'):
        nombre = nombre[:-16] + 'SA'
    elif nombre.endswith(' S.L.L'):
        nombre = nombre[:-5] + 'SLL'
    elif nombre.endswith(' SOCIEDAD LIMITADA LABORAL'):
        nombre = nombre[:-25] + 'SLL'
    elif nombre.endswith(' SOCIEDAD CIVIL PROFESIONAL'):
        nombre = nombre[:-26] + 'SCP'
    elif nombre.endswith(' SOCIEDAD LIMITADA PROFESIONAL'):
        nombre = nombre[:-29] + 'SLP'
    elif nombre.endswith(' S.L.P'):
        nombre = nombre[:-5] + 'SLP'
    elif nombre.endswith(' S. L. P'):
        nombre = nombre[:-7] + 'SLP'
    elif nombre.endswith(' S.L. PROFESIONAL'):
        nombre = nombre[:-16] + 'SLP'
    elif nombre.endswith(' SA UNIPERSONAL'):
        nombre = nombre[:-14] + 'SAU'
    elif nombre.endswith(' S.L UNIPERSONAL'):
        nombre = nombre[:-15] + 'SLU'
    elif nombre.endswith(' SL UNIPERSONAL'):
        nombre = nombre[:-14] + 'SLU'
    elif nombre.endswith(' SOCIEDAD LIMITADA UNIPERSONAL'):
        nombre = nombre[:-29] + 'SLU'
    elif nombre.endswith(' SOCIEDAD LIMITADA NUEVA EMPRESA'):
        nombre = nombre[:-31] + 'SLNE'
    elif nombre.endswith(' S.L.N.E'):
        nombre = nombre[:-7] + 'SLNE'
    elif nombre.endswith(' S.L.N.E.'):
        nombre = nombre[:-8] + 'SLNE'
    elif nombre.endswith(' SOCIEDAD DE RESPONSABILIDAD LIMITADA'):
        nombre = nombre[:-36] + 'SRL'
    elif nombre.endswith(' SOCIEDAD DE RESPONSABILIDAD LIMITADA LABORAL'):
        nombre = nombre[:-44] + 'SRLL'
    elif nombre.endswith(' SOCIEDAD DE RESPONSABILIDAD LIMITADA PROFESIONAL'):
        nombre = nombre[:-48] + 'SRLP'
    elif nombre.endswith(' AGRUPACION DE INTERES ECONOMICO'):
        nombre = nombre[:-31] + 'AIE'
    elif nombre.endswith(' FONDO DE PENSIONES'):
        nombre = nombre[:-18] + 'FP'
    elif nombre.endswith(' SOCIEDAD ANONIMA PROFESIONAL'):
        nombre = nombre[:-28] + 'SAP'

    if nombre.endswith(' S.I.C.A.V. SA'):
        nombre = nombre[:-13] + 'SICAV SA'

    return nombre


def regex_cargos(data, sanitize=True):
    """
    :param data:
    'Adm. Solid.: RAMA SANCHEZ JOSE PEDRO;RAMA SANCHEZ JAVIER JORGE.'
    'Auditor: ACME AUDITORES SL. Aud.Supl.: MACIAS MUÑOZ FELIPE JOSE.'

    :return:

    {'Adm. Solid.': {'RAMA SANCHEZ JOSE PEDRO', 'RAMA SANCHEZ JAVIER JORGE'}}
    {'Auditor': {'ACME AUDITORES SL'}, 'Aud.Supl.': {'MACIAS MUÑOZ FELIPE JOSE'}}
    """
    cargos = {}
    for cargo in re.findall(RE_CARGOS_MATCH, data, re.UNICODE):
        entidades = set()
        for e in cargo[1].split(';'):
            e = e.rstrip('.')
            e = e.strip()
            if sanitize:
                e = regex_nombre_empresa(e)
            entidades.add(e)
        cargos[cargo[0]] = entidades
    return cargos


def regex_decl_unip(data):
    """
    data: "Declaración de unipersonalidad. Socio único: BRENNAN KEVIN LIONEL. Nombramientos."
          "Cambio de identidad del socio único: OLSZEWSKI GRZEGORZ. Ceses/Dimisiones."
    """
    acto_colon, arg_colon, nombreacto, _, nombreacto2 = REGEX_RARE.match(data).groups()  # FIXME: 4º valor None
    if acto_colon == u'Declaración de unipersonalidad. Socio único':
        acto_colon = u'Declaración de unipersonalidad'
    arg_colon = {u'Socio Único': {arg_colon}}
    nombreacto += nombreacto2
    return acto_colon, arg_colon, nombreacto


# TODO: Parser
def regex_escision(nombreacto, data):
    """
    data: "Escisión parcial. Sociedades beneficiarias de la escisión: JUAN SL."
    data: "Escisión total. Sociedades beneficiarias de la escisión: PEDRO ANTONIO 2001 SOCIEDAD LIMITADA. PEDRO ANTONIO EXPLOTACIONES SL."
    """
    if nombreacto == u'Escisión total. Sociedades beneficiarias de la escisión':
        nombreacto = u'Escisión total'
    else:
        data = data.split(u'Sociedades beneficiarias de la escisión: ', 1)[1]
    companies = data.split('. ')
    companies[-1] = companies[-1][:-1]  # Punto final
    beneficiarias = {'Sociedades beneficiarias': set(companies)}
    return nombreacto, beneficiarias


def regex_fusion(data):
    """
    acto: Fusión por unión.
    data: "Sociedades que se fusiónan: YOLO SOCIEDAD ANONIMA."
    """
    if not data.startswith(u'Sociedades que se fusiónan: '):  # SIC
        raise ValueError(data)
    company = data.split(u'Sociedades que se fusiónan: ', 1)[1][:-1]
    return {'Sociedades fusionadas': set([company])}


# This is a way not to use datetime.strftime, which requires es_ES.utf8 locale generated.
def regex_fecha(data):
    """
    Martes 2 de junio de 2015

    >>> REGEX_BORME_FECHA.match(dd).groups()
    ('2', 'junio', '2015')
    """

    day, month, year = re.match('\w+ (\d+) de (\w+) de (\d+)', data).groups()
    return (int(year), MESES[month], int(day))
