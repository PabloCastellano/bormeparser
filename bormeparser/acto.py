#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# seccion.py -
# Copyright (C) 2015 Pablo Castellano <pablo@anche.no>
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

import six

from .utils import acto_to_attr
import pdb; pdb.set_trace()
from .regex import regex_constitucion
regex_constitucion = None


class ACTO:
    NOMBRAMIENTOS = u'Nombramientos'
    REVOCACIONES = u'Revocaciones'
    CESES_DIMISIONES = u'Ceses/Dimisiones'
    MODIFICACIONES_ESTATUTARIAS = u'Modificaciones estatutarias'
    CAMBIO_DE_OBJETO_SOCIAL = u'Cambio de objeto social'
    CAMBIO_DE_DENOMINACION_SOCIAL = u'Cambio de denominación social'
    CAMBIO_DE_DOMICILIO_SOCIAL = u'Cambio de domicilio social'
    AMPLIACION_DEL_OBJETO_SOCIAL = u'Ampliacion del objeto social'
    SOCIEDAD_UNIPERSONAL = u'Sociedad unipersonal'
    DISOLUCION = u'Disolución'
    REELECCIONES = u'Reelecciones'
    CONSTITUCION = u'Constitución'
    ARTICULO_378_5_DEL_RRM = u'Articulo 378.5 del Reglamento del Registro Mercantil'
    OTROS_CONCEPTOS = u'Otros conceptos'
    AMPLIACION_DE_CAPITAL = u'Ampliación de capital'
    REDUCCION_DE_CAPITAL = u'Reducción de capital'
    SITUACION_CONCURSAL = u'Situación concursal'
    FUSION_POR_ABSORCION = u'Fusión por absorción'
    SUSPENSION_DE_PAGOS = u'Suspensión de pagos'
    TRANSFORMACION_DE_SOCIEDAD = u'Transformación de sociedad'
    CANCELACIONES_DE_OFICIO_DE_NOMBRAMIENTOS = u'Cancelaciones de oficio de nombramientos'
    DESEMBOLSO_DE_DIVIDENDOS_PASIVOS = u'Desembolso de dividendos pasivos'
    PAGINA_WEB_DE_LA_SOCIEDAD = u'Página web de la sociedad'
    PRIMERA_SUCURSAL_DE_SOCIEDAD_EXTRANJERA = u'Primera sucursal de sociedad extranjera'
    EXTINCION = u'Extinción'
    PERDIDA_DEL_CARACTER_DE_UNIPERSONALIDAD = u'Pérdida del caracter de unipersonalidad'
    REAPERTURA_HOJA_REGISTRAL = u'Reapertura hoja registral'
    ADAPTACION_LEY_2_95_1 = u'Adaptación Ley 2/95'  # 1
    ADAPTACION_LEY_2_95_2 = u'Adaptada segun D.T. 2 apartado 2 Ley 2/95'  # 2
    CIERRE_PROVISIONAL_BAJA_EN_EL_INDICE_DE_ENTIDADES_JURIDICAS = u'Cierre provisional hoja registral por baja en el índice de Entidades Jurídicas'
    CIERRE_PROVISIONAL_REVOCACION_NIF = u'Cierre provisional de la hoja registral por revocación del NIF'
    REACTIVACION_DE_LA_SOCIEDAD = u'Reactivación de la sociedad (Art. 242 del Reglamento del Registro Mercantil)'
    CAMBIO_DE_IDENTIDAD_DEL_SOCIO_UNICO = u'Cambio de identidad del socio único'
    FE_DE_ERRATAS = u'Fe de erratas'
    DATOS_REGISTRALES = u'Datos registrales'
    CREDITO_INCOBRABLE = u'Crédito incobrable'
    EMPRESARIO_INDIVIDUAL = u'Empresario Individual'
    EMISION_OBLIGACIONES = u'Emisión de obligaciones'
    MODIFICACION_PODERES = u'Modificación de poderes'
    ESCISION_PARCIAL = u'Escisión parcial'
    ESCISION_TOTAL_1 = u'Escisión total. Sociedades beneficiarias de la escisión'  # 1
    ESCISION_TOTAL_2 = u'Escisión total'  # 2
    FUSION_UNION = u'Fusión por unión'
    ADAPTACION_DE_LA_SOCIEDAD = u'Adaptación de sociedad'
    QUIEBRA = u'Quiebra'
    SUCURSAL = u'Sucursal'
    CESION_GLOBAL_ACTIVO_PASIVO = u'Cesión global de activo y pasivo'
    SEGREGACION = u'Segregación'
    ACUERDO_AMPLIACION_CAPITAL_SOCIAL_SIN_EJECUTAR = u'Acuerdo de ampliación de capital social sin ejecutar. Importe del acuerdo'
    MODIFICACION_DE_DURACION = u'Modificación de duración'
    APERTURA_DE_SUCURSAL = u'Apertura de sucursal'
    CIERRE_PROVISIONAL_IMPUESTO_SOCIEDADES = u'Cierre provisional hoja registral art. 137.2 Ley 43/1995 Impuesto de Sociedades'
    DECLARACION_DE_UNIPERSONALIDAD_1 = u'Declaración de unipersonalidad. Socio único'  # 1
    DECLARACION_DE_UNIPERSONALIDAD_2 = u'Declaración de unipersonalidad'  # 2
    PRIMERA_INSCRIPCION = u'Primera inscripcion (O.M. 10/6/1.997)'

    # Palabras clave con argumentos
    ARG_KEYWORDS = [
        NOMBRAMIENTOS, REVOCACIONES, CESES_DIMISIONES, MODIFICACIONES_ESTATUTARIAS,
        CAMBIO_DE_OBJETO_SOCIAL, CAMBIO_DE_DENOMINACION_SOCIAL, CAMBIO_DE_DOMICILIO_SOCIAL,
        AMPLIACION_DEL_OBJETO_SOCIAL, SOCIEDAD_UNIPERSONAL, DISOLUCION, REELECCIONES,
        CONSTITUCION, PRIMERA_INSCRIPCION, APERTURA_DE_SUCURSAL, EMPRESARIO_INDIVIDUAL, ARTICULO_378_5_DEL_RRM,
        OTROS_CONCEPTOS, AMPLIACION_DE_CAPITAL, REDUCCION_DE_CAPITAL, SITUACION_CONCURSAL,
        FUSION_POR_ABSORCION, SUSPENSION_DE_PAGOS, TRANSFORMACION_DE_SOCIEDAD,
        CANCELACIONES_DE_OFICIO_DE_NOMBRAMIENTOS, DESEMBOLSO_DE_DIVIDENDOS_PASIVOS,
        PAGINA_WEB_DE_LA_SOCIEDAD, PRIMERA_SUCURSAL_DE_SOCIEDAD_EXTRANJERA,
        EMISION_OBLIGACIONES, MODIFICACION_PODERES, ESCISION_PARCIAL, ESCISION_TOTAL_1,
        FUSION_UNION, QUIEBRA, SUCURSAL, CESION_GLOBAL_ACTIVO_PASIVO, SEGREGACION
    ]

    # FIXME: SOCIEDAD_UNIPERSONAL esta en arg y noarg
    # Palabras clave sin argumentos
    NOARG_KEYWORDS = [
        CREDITO_INCOBRABLE, EXTINCION, PERDIDA_DEL_CARACTER_DE_UNIPERSONALIDAD, REAPERTURA_HOJA_REGISTRAL,
        ADAPTACION_LEY_2_95_1, ADAPTACION_LEY_2_95_2, CIERRE_PROVISIONAL_BAJA_EN_EL_INDICE_DE_ENTIDADES_JURIDICAS,
        SOCIEDAD_UNIPERSONAL, CIERRE_PROVISIONAL_REVOCACION_NIF, CIERRE_PROVISIONAL_IMPUESTO_SOCIEDADES,
        REACTIVACION_DE_LA_SOCIEDAD, ADAPTACION_DE_LA_SOCIEDAD
    ]

    # Palabras clave seguidas por :
    COLON_KEYWORDS = [
        MODIFICACION_DE_DURACION, FE_DE_ERRATAS
    ]

    RARE_KEYWORDS = [
        CAMBIO_DE_IDENTIDAD_DEL_SOCIO_UNICO, ACUERDO_AMPLIACION_CAPITAL_SOCIAL_SIN_EJECUTAR,
        DECLARACION_DE_UNIPERSONALIDAD_1
    ]

    OTHER_KEYWORDS = [
        DECLARACION_DE_UNIPERSONALIDAD_2, ESCISION_TOTAL_2
    ]

    # Palabra clave
    ENDING_KEYWORDS = [
        DATOS_REGISTRALES
    ]
    
    ALL_KEYWORDS = ARG_KEYWORDS + NOARG_KEYWORDS + COLON_KEYWORDS + RARE_KEYWORDS + OTHER_KEYWORDS + ENDING_KEYWORDS

    @staticmethod
    def get_parser(acto):
        attr = acto_to_attr(acto)
        func = getattr(ActoParser, 'parse_' + attr, ActoParser.parse_default)
        return func

    @staticmethod
    def parse(acto, data):
        func = ACTO.get_parser(acto)
        return func(data)


class ActoParser:

    @staticmethod
    def parse_nombramientos(data):
        pass

    @staticmethod
    def parse_ceses_dimisiones(data):
        return ActoParser.parse_nombramientos(data)

    @staticmethod
    def parse_constitucion(data):
        return regex_constitucion(data)

    @staticmethod
    def parse_primera_inscripcion_o_m(data):
        return ActoParser.parse_constitucion(data)

    @staticmethod
    def parse_default(data):
        print('Using default parser for {0}'.format(data))
        return data

"""
    DICT_KEYWORDS = {kw: remove_accents(kw).replace(' del ', ' ').replace(' por ', ' ').replace(' de ', ' ')
                 .replace(' ', '_').replace('/', '_').replace('.', '_').lower() for kw in ALL_KEYWORDS}

>>> DICT_KEYWORDS.values()
[u'revocaciones', u'cambio_objeto_social', u'reelecciones', u'otros_conceptos', u'fe_erratas', u'sociedad_unipersonal', u'declaracion_unipersonalidad', u'constitucion', u'suspension_pagos', u'
perdida_caracter_unipersonalidad', u'cancelaciones_oficio_nombramientos', u'datos_registrales', u'cambio_domicilio_social', u'disolucion', u'ampliacion_objeto_social', u'cierre_provisional_hoj
a_registral_baja_en_el_indice_entidades_juridicas', u'ceses_dimisiones', u'nombramientos', u'situacion_concursal', u'modificaciones_estatutarias', u'ampliacion_capital', u'adaptacion_ley_2_95'
, u'cambio_denominacion_social', u'extincion', u'reduccion_capital', u'cambio_identidad_socio_unico', u'transformacion_sociedad', u'reapertura_hoja_registral', u'socio_unico', u'articulo_378_5
_reglamento_registro_mercantil', u'fusion_absorcion']
"""
