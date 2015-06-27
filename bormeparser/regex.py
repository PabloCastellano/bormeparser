#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from bormeparser.acto import ACTO
from bormeparser.cargo import CARGO

esc_arg_keywords = [x.replace('.', '\.') for x in ACTO.ALL_KEYWORDS]
esc_colon_keywords = [x.replace('.', '\.') for x in ACTO.COLON_KEYWORDS]
esc_noarg_keywords = [x.replace('.', '\.') for x in ACTO.NOARG_KEYWORDS]
esc_ending_keywords = [x.replace('.', '\.') for x in ACTO.ENDING_KEYWORDS]

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
RE_CARGOS_KEYWORDS = '(%s)' % '|'.join(CARGO.KEYWORDS)
# OR de las palabras clave, "non grouping"
RE_CARGOS_KEYWORDS_NG = '(?:%s)' % '|'.join(CARGO.KEYWORDS)
# RE para capturar el cargo y los nombres
RE_CARGOS_MATCH = RE_CARGOS_KEYWORDS + ':\s([\w+ ;&]+)+\.' + RE_CARGOS_KEYWORDS_NG + '?'
# FIXME: algunos nombres pueden contener caracteres raros como &

REGEX1 = re.compile('^(\d+) - (.*?)\.\s*' + RE_ALL_KEYWORDS_NG)
REGEX2 = re.compile('(?=' + RE_ARG_KEYWORDS + '\.\s+(.*?)\.\s*' + RE_ALL_KEYWORDS_NG + ')')
REGEX3 = re.compile(RE_COLON_KEYWORDS + ':\s+(.*?)\.\s*' + RE_ALL_KEYWORDS_NG)
REGEX4 = re.compile(RE_ENDING_KEYWORD + '\.\s+(.*)\.\s*')
REGEX5 = re.compile(RE_NOARG_KEYWORDS + '\.')

REGEX_EMPRESA = re.compile('^(\d+)\s+-\s+(.*)$')
REGEX_TEXT = re.compile('^\((.*)\)Tj$')
REGEX_BORME_NUM = re.compile('^Núm\. (\d+)')

def regex_cargos(data):
    """
    :param data:
    'Adm. Solid.: RAMA SANCHEZ JOSE PEDRO;RAMA SANCHEZ JAVIER JORGE.'
    'Auditor: ACME AUDITORES SL. Aud.Supl.: MACIAS MUÑOZ FELIPE JOSE.'

    :return:

    [('Adm. Solid.', {'RAMA SANCHEZ JOSE PEDRO', 'RAMA SANCHEZ JAVIER JORGE'})]
    [('Auditor', {'ACME AUDITORES SL'}), ('Aud.Supl.', {'MACIAS MUÑOZ FELIPE JOSE'})]
    """
    cargos = []
    for cargo in re.findall(RE_CARGOS_MATCH, data, re.UNICODE):
        cargos.append((cargo[0], set(cargo[1].split(';'))))
    return cargos
