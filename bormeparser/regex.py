#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# regex.py -
# Copyright (C) 2015-2017 Pablo Castellano <pablo@anche.no>
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


import datetime
import re

from bormeparser.acto import ACTO
from bormeparser.clean import clean_empresa
from bormeparser.cargo import CARGO
from bormeparser.registro import REGISTROS, ALL_REGISTROS
from bormeparser.sociedad import ALL_SOCIEDADES

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)

esc_arg_keywords = [x.replace('.', '\.').replace('(', '\(').replace(')', '\)') for x in ACTO.ARG_KEYWORDS]
esc_colon_keywords = [x.replace('.', '\.') for x in ACTO.COLON_KEYWORDS]
esc_bold_keywords = [x.replace('.', '\.') for x in ACTO.BOLD_KEYWORDS]
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
RE_BOLD_KEYWORDS = '(%s)' % '|'.join(esc_bold_keywords)
RE_ENDING_KEYWORD = '(%s)' % esc_ending_keywords[0]

# -- CARGOS --
# OR de las palabras clave
RE_CARGOS_KEYWORDS = '(%s):' % '|'.join(esc_cargos_keywords)
RE_CARGOS_KEYWORDS2 = '(?=%s|$)' % '|'.join([x + ':' for x in esc_cargos_keywords])
# RE para capturar el cargo y los nombres
RE_CARGOS_MATCH = RE_CARGOS_KEYWORDS + ' (.*?)\.?' + RE_CARGOS_KEYWORDS2

REGEX_NOARG = re.compile(RE_NOARG_KEYWORDS + '\.\s*(.*)', re.UNICODE)
REGEX_ARGCOLON = re.compile(RE_COLON_KEYWORDS + ': (.*?)(?:\.\s+)(.*)', re.UNICODE)
REGEX_BOLD = re.compile(RE_BOLD_KEYWORDS + '\. (.*?)\.\s*' + RE_ALL_KEYWORDS + '(.*)\.?', re.UNICODE)

REGEX_EMPRESA = re.compile('^(\d+) - (.*?)\.?$')
REGEX_EMPRESA_REGISTRO = re.compile('^(\d+) - (.*)\(R.M. (.*)\)\.?$')
REGEX_PDF_TEXT = re.compile('^\((.*)\)Tj$')
REGEX_BORME_NUM = re.compile('^Núm\. (\d+)', re.UNICODE)
REGEX_BORME_FECHA = re.compile('^\w+ (\d+) de (\w+) de (\d+)')
REGEX_BORME_CVE = re.compile('^cve: (.*)$')

MESES = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6, 'julio': 7,
         'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12}


def is_acto_cargo_entrante(data):
    """ Comprueba si es un acto que aporta nuevos cargos """

    if not is_acto_cargo(data):
        raise ValueError('No es un acto con cargos: %s' % data)
    return data in ['Reelecciones', 'Nombramientos']


def is_acto_cargo(data):
    """ Comprueba si es un acto que tiene como parámetro una lista de cargos """
    actos = ['Revocaciones', 'Reelecciones', 'Cancelaciones de oficio de nombramientos', 'Nombramientos',
             'Ceses/Dimisiones', 'Emisión de obligaciones', 'Modificación de poderes']
    return data in actos


def is_acto_noarg(data):
    """ Comprueba si es un acto que no tiene parametros """
    return data in ACTO.NOARG_KEYWORDS


def is_acto_bold_mix(data):
    return data.startswith('Escisión total')


def is_acto_bold(data):
    for acto in ACTO.BOLD_KEYWORDS:
        if data.startswith(acto):
            return True
    return False


def is_company(data):
    """ Comprueba si es algún tipo de sociedad o por el contrario es una persona física """
    siglas = ALL_SOCIEDADES
    siglas = list(map(lambda x: ' %s' % x, siglas))
    data = clean_empresa(data)
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


def regex_empresa_tipo(data):
    """
        data: "GRUAS BANCALERO SL"
        return empresa: "GRUAS BANCALERO"
        return tipo: "SL"
    """
    empresa = clean_empresa(data)
    tipo = ''
    for t in ALL_SOCIEDADES:
        if empresa.endswith(' %s' % t):
            empresa = empresa[:-len(t) - 1]
            tipo = t
            empresa = empresa.rstrip(",")
    return empresa, tipo


def regex_empresa(data, sanitize=True):
    """ Captura el número de acto y el nombre de la empresa
        Si el nombre incluye el nombre de un registro mercantil, lo devuelve en el tercer parámetro
        El tercer parámetro contiene información extra de la empresa

        data: "57344 - ALDARA CATERING SL"
        data: "473700 - SA COVA PLAÇA MAJOR SL(R.M. PALMA DE MALLORCA)"
    """

    extra = {"liquidacion": False, "sucursal": False, "registro": ""}
    res = REGEX_EMPRESA_REGISTRO.match(data)
    if res:
        acto_id, empresa, registro = res.groups()
        if registro not in ALL_REGISTROS:
            logger.warning("Registro desconocido: " + registro)
        else:
            extra["registro"] = REGISTROS[registro]
    else:
        acto_id, empresa = REGEX_EMPRESA.match(data).groups()
        registro = None

    if empresa.endswith(" EN LIQUIDACION"):
        extra["liquidacion"] = True
        empresa = re.sub(" EN LIQUIDACION$", "", empresa)

    if empresa.endswith(" SUCURSAL EN ESPAÑA"):
        extra["sucursal"] = True
        empresa = re.sub(" SUCURSAL EN ESPAÑA$", "", empresa)

    if sanitize:
        empresa = clean_empresa(empresa)
    return int(acto_id), empresa, extra


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
            e = e.strip(" .")
            if sanitize:
                e = clean_empresa(e)
            entidades.add(e)
        if cargo[0] in cargos:
            cargos[cargo[0]].update(entidades)
        else:
            cargos[cargo[0]] = entidades
    return cargos


def regex_bold_acto(data):
    """
    data: "Declaración de unipersonalidad. Socio único: BRENNAN KEVIN LIONEL. Nombramientos."
          "Sociedad unipersonal. Cambio de identidad del socio único: OLSZEWSKI GRZEGORZ. Ceses/Dimisiones."
    """
    acto_colon, arg_colon, nombreacto, nombreacto2 = REGEX_BOLD.match(data).groups()
    nombreacto += nombreacto2
    return acto_colon, arg_colon, nombreacto


def regex_constitucion(data):

    def parse_capital(amount):
        # '3.000,00 Euros', '3.000.000 Ptas'
        amount = amount.group(1).strip()
        if 'Euros' in amount:
            amount = amount.split(' Euros')[0]
            amount = float(amount.replace('.', '').replace(',', '.'))
        elif 'Ptas' in amount:
            amount = amount.split(' Ptas')[0]
            amount = int(amount.replace('.', ''))
        else:
            raise ValueError('Capital ni Ptas ni Euros: {0}'.format(amount))
        return amount

    all_keywords = ['Comienzo de operaciones', 'Duración', 'Objeto social', 'Domicilio'
                    'Capital', 'Capital suscrito', 'Desembolsado']
    all_keywords.append('$')
    all_or_ng = '(?:{0})'.format('|'.join(all_keywords))

    date = re.search('Comienzo de operaciones: (.*?){0}'.format(all_or_ng), data).group(1).strip()
    if len(date) > 1 and date[1] == '.':
        date = date[:7]
    elif len(date) > 2 and date[2] == '.':
        date = date[:8]
    if date.endswith('.'):
        date = date[:-1]
    try:
        # 'dd.mm.yy', 'd.mm.yy', 'dd.m.yy', 'd.m.yy', 'dd/mm/yy', '2-10-2009', '21 DE FEBRERO DE 2006'
        if '/' in date or '-' in date:
            n = re.findall('(\d{1,4})', date)  # ['17', '04', '2013']
            if len(n) != 3:
                raise ValueError
            date = {'day': int(n[0]), 'month': int(n[1]), 'year': int(n[2])}
            date = datetime.date(**date)
        elif ' de ' in date.lower():
            match = re.match('(\d+) de (\w+) de (\d+)', date.lower())
            if not match:
                raise ValueError
            day, month, year = match.groups()
            date = datetime.date(day=int(day), month=MESES[month], year=int(year))
        else:
            date = datetime.datetime.strptime(date, '%d.%m.%y').date()
        date = date.isoformat()
    except ValueError:
        print('ERROR CON Comienzo de operaciones: {0}'.format(date))

    duration = re.search('Duración: (.*?){0}'.format(all_or_ng), data)
    if duration:
        duration = duration.group(1).strip()

    activity = re.search('Objeto social: (.*?){0}'.format(all_or_ng), data)
    if activity:
        activity = activity.group(1).strip()
        activity = capitalize_sentence(activity)

    address = re.search('Domicilio: (.*?){0}'.format(all_or_ng), data)
    if address:
        address = address.group(1).strip().title()

    capital = re.search('Capital: (.*?){0}'.format(all_or_ng), data)
    if capital:
        try:
            capital = parse_capital(capital)
        except ValueError:
            raise ValueError('Capital ni Ptas ni Euros: {0}'.format(capital))

    suscrito = re.search('Capital suscrito: (.*?){0}'.format(all_or_ng), data)
    if suscrito:
        try:
            suscrito = parse_capital(suscrito)
        except ValueError:
            raise ValueError('Suscrito ni Ptas ni Euros: {0}'.format(suscrito))

    desembolsado = re.search('Desembolsado: (.*?){0}'.format(all_or_ng), data)
    if desembolsado:
        try:
            desembolsado = parse_capital(desembolsado)
        except ValueError:
            raise ValueError('Desembolsado ni Ptas ni Euros: {0}'.format(desembolsado))

    return (date, activity, address, capital)


# This is a way not to use datetime.strftime, which requires es_ES.utf8 locale generated.
def regex_fecha(data):
    """
    Martes 2 de junio de 2015

    >>> REGEX_BORME_FECHA.match(dd).groups()
    ('2', 'junio', '2015')
    """

    day, month, year = re.match('\w+ (\d+) de (\w+) de (\d+)', data, re.UNICODE).groups()
    return (int(year), MESES[month], int(day))


def borme_c_separa_empresas_titulo(titulo):
    """ This function is far from being perfect """
    #
    #        if len(empresas) > 0:
    #            # ['SOCIEDAD ANONIMA BLABLA (SOCIEDAD ABSORBENTE)', ' CABALUR, SOCIEDAD LIMITADA UNIPERSONAL (SOCIEDAD ABSORBIDA)']
    #            # ['MONTE ALMACABA, S.L. (SOCIEDAD BENEFICIARIA DE LA ESCISION DE NUEVA CREACION)', ' AGROPECUARIA SANTA MARIA DE LA CABEZAS S.L. (SOCIEDAD QUE SE ESCINDE PARCIALMENTE)']
    #            empresas = list(map(lambda x: re.sub('\(.*?\)', '', x), empresas))
    #            empresas = list(map(lambda x: x.strip(), empresas))
    #            # ['MONTE ALMACABA, S.L.', 'AGROPECUARIA SANTA MARIA DE LA CABEZAS,S.L.']
    #            empresa = empresas[0]
    #            relacionadas = empresas[1:]
    #
    empresas = []
    lines = []

    if not '\n' in titulo:
        lines = re.findall('.*? \([\w\s]+\)', titulo, re.UNICODE)
    if len(lines) == 0:
        lines = titulo.split('\n')

    for line in lines:
        empresa = re.sub('\(.*?\)', '', line)
        #empresa = line.replace('(SOCIEDAD ABSORBENTE)', '')
        #empresa = empresa.replace('(SOCIEDAD ABSORBIDA)', '')
        #empresa = empresa.replace('(SOCIEDAD ESCINDIDA)', '')
        #empresa = empresa.replace('(SOCIEDAD BENEFICIARIA)', '')
        #empresa = empresa.replace('(SOCIEDADES ABSORBIDAS)', '')
        #empresa = empresa.replace('(EN LIQUIDACIÓN)', '')
        #empresa = empresa.replace('(SOCIEDAD ABSORBENTE Y PARCIALMENTE ESCINDIDA)', '')
        #empresa = empresa.replace('(SOCIEDADES BENEFICIARIAS DE LA ESCISIÓN PARCIAL)', '')
        empresa = empresa.replace('SOCIEDAD ABSORBENTE', '')
        empresa = empresa.replace('SOCIEDAD ABSORBIDA', '')
        empresa = empresa.strip()
        empresa = empresa.rstrip(',')
        empresa = empresa.strip()
        empresas.append(empresa)
        # TODO: regex_empresa

    if len(empresas) > 1:
        # ['COEMA']
        empresas = [e for e in empresas if len(e) > 4]

    return empresas


def capitalize_sentence(string):
    # TODO: espacio de más tras coma/punto
    string = re.sub(r'([,/\.]+)(?! )', r'\1 ', string)
    if string == string.upper():
        string = string.lower()
    sentences = string.split(". ")
    while '' in sentences:
        sentences.remove('')
    sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
    string2 = '. '.join(sentences2)
    if not string2.endswith('.'):
        string2 += '.'

    return string2
