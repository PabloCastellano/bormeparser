#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# sociedad.py -
# Copyright (C) 2015-2022 Pablo Castellano <pablo@anche.no>
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


# https://es.wikipedia.org/wiki/Anexo:Tipos_de_sociedad_mercantil_en_Espa%C3%B1a
SOCIEDADES = {
    'AIE': 'Agrupación de Interés Económico',
    'AEIE': 'Agrupación Europea de Interés Económico',
    'COOP': 'Cooperativa',
    'FP': 'Fondo de Pensiones',
    'SA': 'Sociedad Anónima',
    'SAD': 'Sociedad Anónima Deportiva',
    'SAL': 'Sociedad Anónima Laboral',
    'SAP': 'Sociedad Anónima P?',
    'SAS': 'Sociedad por Acciones Simplificada',
    'SAU': 'Sociedad Anónima Unipersonal',
    'SC': 'Sociedad Colectiva',
    'S.COM.': 'Sociedad Comanditaria',
    'S.COM.P.A.': 'Sociedad Comanditaria por Acciones',
    'SCP': 'Sociedad Civil Profesional',
    'SICAV': 'Sociedad de Inversión de Capital Variable',
    'SL': 'Sociedad Limitada',
    'SLL': 'Sociedad Limitada Laboral',
    'SLLP': 'Sociedad Limitada Laboral P?',
    'SLNE': 'Sociedad Limitada Nueva Empresa',
    'SLP': 'Sociedad Limitada Profesional',
    'SLU': 'Sociedad Limitada Unipersonal',
    'SME': 'Sociedad Mercantil Estatal',
    'SRL': 'Sociedad de Responsabilidad Limitada',
    'SRLL': 'Sociedad de Responsabilidad Limitada Laboral',
    'SRLP': 'Sociedad de Responsabilidad Limitada Profesional',
}
# SOCIEDAD COOPERATIVA DE CREDITO
# FONDOS DE PENSIONES

# Tipos de sociedades extranjeras
SOCIEDADES.update({
    # Bélgica
    # BVBA: Sociedad Privada de Responsabilidad Limitada
    'BVBA': 'Besloten vennootschap met beperkte aansprakelijkheid',

    # Holanda
    # BV: Sociedad Privada de Responsabilidad Limitada
    'BV': 'Besloten vennootschap met beperkte aansprakelijkheid',
    # NV: Sociedad Anónima (Holanda)
    'NV': 'Naamloze Vennootschap',

    # UK
    'LTD': 'Limited company',
})

ALL_SOCIEDADES = sorted(SOCIEDADES.keys())
