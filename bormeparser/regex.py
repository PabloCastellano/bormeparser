#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from bormeparser.acto import ACTO
from bormeparser.cargo import CARGO

esc_arg_keywords = [x.replace('.', '\.') for x in ACTO.ALL_KEYWORDS]
esc_colon_keywords = [x.replace('.', '\.') for x in ACTO.COLON_KEYWORDS]
esc_noarg_keywords = [x.replace('.', '\.').replace('(', '\(').replace(')', '\)') for x in ACTO.NOARG_KEYWORDS]
esc_ending_keywords = [x.replace('.', '\.') for x in ACTO.ENDING_KEYWORDS]

esc_cargos_keywords = [x.replace('.', '\.') for x in CARGO.KEYWORDS]

# -- ACTOS --
# OR de las palabras clave con argumentos
RE_ARG_KEYWORDS = '(%s)' % '|'.join(esc_arg_keywords)
# OR de las palabras clave, "non grouping"
RE_ALL_KEYWORDS_NG = '(?:%s|%s|%s|%s)' % ('|'.join(esc_arg_keywords), '|'.join(esc_colon_keywords),
                                          '|'.join(esc_noarg_keywords), esc_ending_keywords[0])
# OR de las palabras clave sin argumentos
RE_NOARG_KEYWORDS = '(%s)' % '|'.join(esc_noarg_keywords)
# OR de las palabras clave con argumentos seguidas por :
RE_COLON_KEYWORDS = '(%s)' % '|'.join(esc_colon_keywords)
RE_ENDING_KEYWORD = '(%s)' % esc_ending_keywords[0]

# -- CARGOS --
# OR de las palabras clave
RE_CARGOS_KEYWORDS = '(%s)' % '|'.join(esc_cargos_keywords)
# RE para capturar el cargo y los nombres
RE_CARGOS_MATCH = RE_CARGOS_KEYWORDS + ":\s(.*?)(?:\.$|\. )"

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

REGEX_EMPRESA = re.compile('^(\d+)\s+-\s+(.*?)(?:\.$|$)')
REGEX_TEXT = re.compile('^\((.*)\)Tj$')
REGEX_BORME_NUM = re.compile(u'^Núm\. (\d+)', re.UNICODE)
REGEX_BORME_FECHA = re.compile('^\w+ (\d+) de (\w+) de (\d+)')
REGEX_BORME_CVE = re.compile('^cve: (.*)$')

MESES = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6, 'julio': 7,
         'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12}


# https://es.wikipedia.org/wiki/Anexo:Tipos_de_sociedad_mercantil_en_Espa%C3%B1a
SOCIEDADES = {'SA': 'Sociedad Anónima',
              'SL': 'Sociedad Limitada',
              'SLU': 'Sociedad Limitada Unipersonal',
              'SLP': 'Sociedad Limitada Profesional',
              'SRL': 'Sociedad de Responsabilidad Limitada',
              'AIE': 'Agrupación de Interés Económico',
              'COOP': 'Cooperativa',
              'SLL': 'Sociedad Limitada Laboral',
              'SAL': 'Sociedad Anónima Laboral',
              'SLNE': 'Sociedad Limitada Nueva Empresa'
              }


def is_acto_cargo_entrante(data):
    """ Comprueba si es un acto que aporta nuevos cargos """

    if not is_acto_cargo(data):
        raise ValueError('No es un acto con cargos: %s' % data)
    return data in ['Reelecciones', 'Nombramientos']


# TODO: Comprobar que son todos
def is_acto_cargo(data):
    """ Comprueba si es un acto que tiene como parámetro una lista de cargos """
    actos = ['Revocaciones', 'Reelecciones', 'Cancelaciones de oficio de nombramientos', 'Nombramientos', 'Ceses/Dimisiones',
             u'Declaración de unipersonalidad. Socio único', u'Cambio de identidad del socio único',
             u'Emisión de obligaciones', u'Modificación de poderes']
    return data in actos


def is_acto_noarg(data):
    """ Comprueba si es un acto que no tiene parametros """
    return data in ACTO.NOARG_KEYWORDS


# TODO: Añadir otras sociedades menos usuales
def is_company(data):
    """ Comprueba si es algún tipo de sociedad o por el contrario es una persona física """
    siglas = list(SOCIEDADES.keys())
    siglas.extend(['SOCIEDAD LIMITADA', 'SOCIEDAD ANONIMA'])
    siglas = list(map(lambda x: ' %s' % x, siglas))
    return any(data.endswith(s) for s in siglas)


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


def regex_empresa(data):
    """ Captura el número de acto y el nombre de la empresa """
    acto_id, empresa = REGEX_EMPRESA.match(data).groups()
    return int(acto_id), empresa


def regex_cargos(data):
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
        cargos[cargo[0]] = set(cargo[1].split(';'))
    return cargos


# This is a way not to use datetime.strftime, which requires es_ES.utf8 locale generated.
def regex_fecha(data):
    """
    Martes 2 de junio de 2015

    >>> REGEX_BORME_FECHA.match(dd).groups()
    ('2', 'junio', '2015')
    """

    day, month, year = re.match('\w+ (\d+) de (\w+) de (\d+)', data).groups()
    return (int(year), MESES[month], int(day))
