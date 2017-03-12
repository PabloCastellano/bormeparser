#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# clean.py -
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
import re

SIGLAS = {
    "S.L": "SL",
    "S L": "SL",
    "SOCIEDAD LIMITADA": "SL",
    "SOCIETAT LIMITADA": "SL",
    "SOCIEDAD ANONIMA DEPORTIVA": "SAD",
    "S.A.L": "SAL",
    "SOCIEDAD ANONIMA LABORAL": "SAL",
    "S.A": "SA",
    "B.V": "BV",
    "N.V": "NV",
    "SOCIEDAD ANONIMA": "SA",
    "S L L": "SLL",
    "S.L.L": "SLL",
    "SOCIEDAD LIMITADA LABORAL": "SLL",
    "SOCIEDAD CIVIL PROFESIONAL": "SCP",
    "SOCIEDAD LIMITADA PROFESIONAL": "SLP",
    "S.L.P": "SLP",
    "S. L. P": "SLP",
    "S.L. PROFESIONAL": "SLP",
    "SA UNIPERSONAL": "SAU",
    "S.L UNIPERSONAL": "SLU",
    "SL UNIPERSONAL": "SLU",
    "SOCIEDAD LIMITADA UNIPERSONAL": "SLU",
    "SOCIEDAD LIMITADA NUEVA EMPRESA": "SLNE",
    "S.L.N.E": "SLNE",
    "SOCIEDAD DE RESPONSABILIDAD LIMITADA": "SRL",
    "SOCIEDAD DE RESPONSABILIDAD LIMITADA LABORAL": "SRLL",
    "SOCIEDAD DE RESPONSABILIDAD LIMITADA PROFESIONAL": "SRLP",
    "A.I.E": "AIE",
    "AGRUPACION DE INTERES ECONOMICO": "AIE",
    "FONDO DE PENSIONES": "FP",
    "SOCIEDAD ANONIMA PROFESIONAL": "SAP",
    "SOCIEDAD COMANDITARIA": "SC",
    "SOCIEDAD COMANDITARIA SIMPLE": "SC",  # SC simple
    "SOCIEDAD COMANDITARIA POR ACCIONES": "SC",  # SC por acciones
    "LIMITED": "LTD",
    "SOCIEDAD MERCANTIL ESTATAL": "SME",
    "SOCIEDAD ANONIMA DE INVERSION DE CAPITAL VARIABLE": "SICAV",
    "S.I.C.A.V. SA": "SICAV",
    "SA SICAV": "SICAV",
}


# TODO: UNION TEMPORAL DE EMPRESAS LEY 18 1982 DE 26 DE MAYO
def clean_empresa(nombre):
    nombre = nombre.rstrip(".")
    sucursal_spain = False

    for sigla in SIGLAS.keys():
        regexp = " " + sigla.replace(".", "\.") + "$"
        nombre = re.sub(regexp, " " + SIGLAS[sigla], nombre)

    return nombre
