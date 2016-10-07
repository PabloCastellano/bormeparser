#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# clean.py -
# Copyright (C) 2015-2016 Pablo Castellano <pablo@anche.no>
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


# TODO: Devolver palabras clave como SICAV, SUCURSAL EN ESPAÑA, EN LIQUIDACION
# UNION TEMPORAL DE EMPRESAS LEY 18 1982 DE 26 DE MAYO
def clean_empresa(nombre):
    sucursal_spain = False

    if nombre.endswith(' S.L'):
        nombre = nombre[:-3] + 'SL'
    if nombre.endswith(' S L'):
        nombre = nombre[:-3] + 'SL'
    elif nombre.endswith(' SOCIEDAD LIMITADA'):
        nombre = nombre[:-17] + 'SL'
    elif nombre.endswith(' SOCIETAT LIMITADA'):
        nombre = nombre[:-17] + 'SL'
    elif nombre.endswith(' SOCIEDAD ANONIMA DEPORTIVA'):
        nombre = nombre[:-26] + 'SAD'
    elif nombre.endswith(' S.A.L'):
        nombre = nombre[:-5] + 'SAL'
    elif nombre.endswith(' SOCIEDAD ANONIMA LABORAL'):
        nombre = nombre[:-24] + 'SAL'
    elif nombre.endswith(' S.A'):
        nombre = nombre[:-3] + 'SA'
    elif nombre.endswith(' B.V'):
        nombre = nombre[:-3] + 'BV'
    elif nombre.endswith(' N.V'):
        nombre = nombre[:-3] + 'NV'
    elif nombre.endswith(' SOCIEDAD ANONIMA'):
        nombre = nombre[:-16] + 'SA'
    elif nombre.endswith(' S L L'):
        nombre = nombre[:-5] + 'SLL'
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
    elif nombre.endswith(' SOCIEDAD DE RESPONSABILIDAD LIMITADA'):
        nombre = nombre[:-36] + 'SRL'
    elif nombre.endswith(' SOCIEDAD DE RESPONSABILIDAD LIMITADA LABORAL'):
        nombre = nombre[:-44] + 'SRLL'
    elif nombre.endswith(' SOCIEDAD DE RESPONSABILIDAD LIMITADA PROFESIONAL'):
        nombre = nombre[:-48] + 'SRLP'
    elif nombre.endswith(' A.I.E'):
        nombre = nombre[:-5] + 'AIE'
    elif nombre.endswith(' AGRUPACION DE INTERES ECONOMICO'):
        nombre = nombre[:-31] + 'AIE'
    elif nombre.endswith(' FONDO DE PENSIONES'):
        nombre = nombre[:-18] + 'FP'
    elif nombre.endswith(' SOCIEDAD ANONIMA PROFESIONAL'):
        nombre = nombre[:-28] + 'SAP'
    elif nombre.endswith(' SOCIEDAD COMANDITARIA'):
        nombre = nombre[:-21] + 'SC'
    elif nombre.endswith(' SOCIEDAD COMANDITARIA SIMPLE'):  # SC simple
        nombre = nombre[:-28] + 'SC'
    elif nombre.endswith(' SOCIEDAD COMANDITARIA POR ACCIONES'):  # SC por acciones
        nombre = nombre[:-34] + 'SC'
    elif nombre.endswith(' A.E.I.E'):
        nombre = nombre[:-7] + 'AEIE'

    if nombre.endswith(' SOCIEDAD ANONIMA DE INVERSION DE CAPITAL VARIABLE'):
        nombre = nombre[:-49] + 'SICAV'
    if nombre.endswith(' S.I.C.A.V. SA'):
        nombre = nombre[:-13] + 'SICAV'
    if nombre.endswith(' SA SICAV'):
        nombre = nombre[:-8] + 'SICAV'

    return nombre
