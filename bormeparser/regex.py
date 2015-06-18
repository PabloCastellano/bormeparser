import re

from bormeparser.acto import ACTO
from bormeparser.cargo import CARGO

# OR de las palabras clave con argumentos
RE_ARG_KEYWORDS = '(%s)' % '|'.join(ACTO.ARG_KEYWORDS)
# OR de todas las palabras clave, "non grouping"
RE_ALL_KEYWORDS_NG = '(?:%s|%s|%s|%s)' % ('|'.join(ACTO.ARG_KEYWORDS), '|'.join(ACTO.COLON_KEYWORDS), '|'.join(ACTO.NOARG_KEYWORDS), ACTO.ENDING_KEYWORDS[0])
# OR de las palabras clave sin argumentos
RE_NOARG_KEYWORDS = '(%s)' % '|'.join(ACTO.NOARG_KEYWORDS)
# OR de las palabras clave con argumentos seguidas por :
RE_COLON_KEYWORDS = '(%s)' % '|'.join(ACTO.COLON_KEYWORDS)
RE_ENDING_KEYWORD = '(%s)' % ACTO.ENDING_KEYWORDS[0]

# Cargos
RE_CARGOS_KEYWORDS = '(%s)' % '|'.join(CARGO.CARGOS_KEYWORDS)
RE_CARGOS_KEYWORDS_NG = '(?:%s)' % '|'.join(CARGO.CARGOS_KEYWORDS)
RE_CARGOS_MATCH = RE_CARGOS_KEYWORDS + ':\s([\w+ ;]+)+\.' + RE_CARGOS_KEYWORDS_NG + '?'

# TODO: Escapar por puntos (. por \.)

REGEX1 = re.compile('^(\d+) - (.*?)\.\s*' + RE_ALL_KEYWORDS_NG)
REGEX2 = re.compile('(?=' + RE_ARG_KEYWORDS + '\.\s+(.*?)\.\s*' + RE_ALL_KEYWORDS_NG + ')')
REGEX3 = re.compile(RE_COLON_KEYWORDS + ':\s+(.*?)\.\s*' + RE_ALL_KEYWORDS_NG)
REGEX4 = re.compile(RE_ENDING_KEYWORD + '\.\s+(.*)\.\s*')
REGEX5 = re.compile(RE_NOARG_KEYWORDS + '\.')


def regex_cargos(data):
    """
    [('Auditor', 'ACME AUDITORES SL'), ('Aud.Supl.', 'MACIAS MUÑOZ FELIPE JOSE')]
    [('Adm. Solid.', 'RAMA SANCHEZ JOSE PEDRO;RAMA SANCHEZ JAVIER JORGE')]

    :param data:
    :return:
    """
    cargos = []
    for cargo in re.findall(RE_CARGOS_MATCH, data):
        cargos.append((cargo[0], set(cargo[1].split(';'))))
    return cargos