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


class ACTO:
    NOMBRAMIENTOS = 1
    REVOCACIONES = 2
    CESES_DIMISIONES = 3
    MODIFICACIONES_ESTATUTARIAS = 4
    CAMBIO_DE_OBJETO_SOCIAL = 5
    CAMBIO_DE_DENOMINACION_SOCIAL = 6
    CAMBIO_DE_DOMICILIO_SOCIAL = 7
    AMPLIACION_DEL_OBJETO_SOCIAL = 8
    SOCIEDAD_UNIPERSONAL = 9
    DISOLUCION = 10
    REELECCIONES = 11
    CONSTITUCION = 12
    ARTICULO_378_5_DEL_RRM = 13
    OTROS_CONCEPTOS = 14
    AMPLIACION_DE_CAPITAL = 15
    REDUCCION_DE_CAPITAL = 16
    SITUACION_CONCURSAL = 17
    FUSION_POR_ABSORCION = 18
    SUSPENSION_DE_PAGOS = 19
    TRANSFORMACION_DE_SOCIEDAD = 20
    CANCELACIONES_DE_OFICIO_DE_NOMBRAMIENTOS = 21
    DESEMBOLSO_DE_DIVIDENDOS_PASIVOS = 22
    PAGINA_WEB_DE_LA_SOCIEDAD = 23
    PRIMERA_SUCURSAL_DE_SOCIEDAD_EXTRANJERA = 24

    EXTINCION = 26
    DECLARACION_DE_UNIPERSONALIDAD = 27
    PERDIDA_DEL_CARACTER_DE_UNIPERSONALIDAD = 28
    REAPERTURA_HOJA_REGISTRAL = 29
    ADAPTACION_LEY_2_95 = 30
    CIERRE_PROVISIONAL_BAJA_EN_EL_INDICE_DE_ENTIDADES_JURIDICAS = 31
    CIERRE_PROVISIONAL_REVOCACION_NIF = 32
    REACTIVACION_DE_LA_SOCIEDAD = 32

    FE_DE_ERRATAS = 34
    DATOS_REGISTRALES = 35
    CREDITO_INCOBRABLE = 36
    EMPRESARIO_INDIVIDUAL = 37
    EMISION_OBLIGACIONES = 38
    MODIFICACION_PODERES = 39
    ESCISION_PARCIAL = 40
    ESCISION_TOTAL = 41
    FUSION_UNION = 42
    ADAPTACION_DE_LA_SOCIEDAD = 43
    QUIEBRA = 44
    SUCURSAL = 45
    CESION_GLOBAL_ACTIVO_PASIVO = 46
    SEGREGACION = 47
    ACUERDO_AMPLIACION_CAPITAL_SOCIAL_SIN_EJECUTAR = 48
    MODIFICACION_DE_DURACION = 49
    APERTURA_DE_SUCURSAL = 50
    CIERRE_PROVISIONAL_IMPUESTO_SOCIEDADES = 51
    PRIMERA_INSCRIPCION = 52
    ANOTACION_PREVENTIVA_DEMANDA = 53
    ANOTACION_PREVENTIVA_DECLARACION = 54
    CIERRE_SUCURSAL = 55
    ADAPTACION_LEY_44_2015 = 56

    # Palabras clave con argumentos
    _arg_keywords = {
        'Nombramientos': NOMBRAMIENTOS,
        'Revocaciones': REVOCACIONES,
        'Ceses/Dimisiones': CESES_DIMISIONES,
        'Modificaciones estatutarias': MODIFICACIONES_ESTATUTARIAS,
        'Cambio de objeto social': CAMBIO_DE_OBJETO_SOCIAL,
        'Cambio de denominación social': CAMBIO_DE_DENOMINACION_SOCIAL,
        'Cambio de domicilio social': CAMBIO_DE_DOMICILIO_SOCIAL,
        'Ampliacion del objeto social': AMPLIACION_DEL_OBJETO_SOCIAL,
        'Disolución': DISOLUCION,
        'Reelecciones': REELECCIONES,
        'Constitución': CONSTITUCION,
        'Apertura de sucursal': APERTURA_DE_SUCURSAL,
        'Empresario Individual': EMPRESARIO_INDIVIDUAL,
        'Articulo 378.5 del Reglamento del Registro Mercantil': ARTICULO_378_5_DEL_RRM,
        'Otros conceptos': OTROS_CONCEPTOS,
        'Ampliación de capital': AMPLIACION_DE_CAPITAL,
        'Reducción de capital': REDUCCION_DE_CAPITAL,
        'Situación concursal': SITUACION_CONCURSAL,
        'Fusión por absorción': FUSION_POR_ABSORCION,
        'Suspensión de pagos': SUSPENSION_DE_PAGOS,
        'Transformación de sociedad': TRANSFORMACION_DE_SOCIEDAD,
        'Cancelaciones de oficio de nombramientos': CANCELACIONES_DE_OFICIO_DE_NOMBRAMIENTOS,
        'Desembolso de dividendos pasivos': DESEMBOLSO_DE_DIVIDENDOS_PASIVOS,
        'Página web de la sociedad': PAGINA_WEB_DE_LA_SOCIEDAD,
        'Primera sucursal de sociedad extranjera': PRIMERA_SUCURSAL_DE_SOCIEDAD_EXTRANJERA,
        'Emisión de obligaciones': EMISION_OBLIGACIONES,
        'Modificación de poderes': MODIFICACION_PODERES,
        'Escisión parcial': ESCISION_PARCIAL,
        'Fusión por unión': FUSION_UNION,
        'Quiebra': QUIEBRA,
        'Sucursal': SUCURSAL,
        'Cesión global de activo y pasivo': CESION_GLOBAL_ACTIVO_PASIVO,
        'Segregación': SEGREGACION,
        'Primera inscripcion (O.M. 10/6/1.997)': PRIMERA_INSCRIPCION,
        'Anotación preventiva. Demanda de impugnación de acuerdos sociales': ANOTACION_PREVENTIVA_DEMANDA,
        'Anotación preventiva. Declaración de deudor fallido': ANOTACION_PREVENTIVA_DECLARACION,
    }

    # Palabras clave sin argumentos
    _noarg_keywords = {
        'Crédito incobrable': CREDITO_INCOBRABLE,
        'Sociedad unipersonal': SOCIEDAD_UNIPERSONAL,
        'Extinción': EXTINCION,
        'Pérdida del caracter de unipersonalidad': PERDIDA_DEL_CARACTER_DE_UNIPERSONALIDAD,
        'Reapertura hoja registral': REAPERTURA_HOJA_REGISTRAL,
        'Adaptación Ley 2/95': ADAPTACION_LEY_2_95,
        'Adaptación Ley 44/2015': ADAPTACION_LEY_44_2015,
        'Adaptada segun D.T. 2 apartado 2 Ley 2/95': ADAPTACION_LEY_2_95,
        'Cierre provisional hoja registral por baja en el índice de Entidades Jurídicas': CIERRE_PROVISIONAL_BAJA_EN_EL_INDICE_DE_ENTIDADES_JURIDICAS,
        'Cierre provisional de la hoja registral por revocación del NIF': CIERRE_PROVISIONAL_REVOCACION_NIF,
        'Cierre provisional hoja registral por revocación del NIFde Entidades Jurídicas': CIERRE_PROVISIONAL_REVOCACION_NIF,
        'Cierre provisional hoja registral art. 137.2 Ley 43/1995 Impuesto de Sociedades': CIERRE_PROVISIONAL_IMPUESTO_SOCIEDADES,
        'Reactivación de la sociedad (Art. 242 del Reglamento del Registro Mercantil)': REACTIVACION_DE_LA_SOCIEDAD,
        'Adaptación de sociedad': ADAPTACION_DE_LA_SOCIEDAD,
        'Cierre de Sucursal': CIERRE_SUCURSAL,
    }

    # Palabras clave seguidas por :
    _colon_keywords = {
        'Modificación de duración': MODIFICACION_DE_DURACION,
        'Fe de erratas': FE_DE_ERRATAS,
    }

    _bold_keywords = {
        'Declaración de unipersonalidad': DECLARACION_DE_UNIPERSONALIDAD,
        'Sociedad unipersonal': SOCIEDAD_UNIPERSONAL,
        'Acuerdo de ampliación de capital social sin ejecutar. Importe del acuerdo': ACUERDO_AMPLIACION_CAPITAL_SOCIAL_SIN_EJECUTAR,
        'Escisión total': ESCISION_TOTAL,
    }

    # Palabra clave
    _ending_keywords = {
        'Datos registrales': DATOS_REGISTRALES
    }

    ARG_KEYWORDS = list(_arg_keywords.keys())
    NOARG_KEYWORDS = list(_noarg_keywords.keys())
    COLON_KEYWORDS = list(_colon_keywords.keys())
    BOLD_KEYWORDS = list(_bold_keywords.keys())
    ENDING_KEYWORDS = list(_ending_keywords.keys())
    ALL_KEYWORDS = ARG_KEYWORDS + NOARG_KEYWORDS + COLON_KEYWORDS + BOLD_KEYWORDS + ENDING_KEYWORDS

"""
    DICT_KEYWORDS = {kw: remove_accents(kw).replace(' del ', ' ').replace(' por ', ' ').replace(' de ', ' ')
                 .replace(' ', '_').replace('/', '_').replace('.', '_').lower() for kw in ALL_KEYWORDS}

>>> DICT_KEYWORDS.values()
['revocaciones', 'cambio_objeto_social', 'reelecciones', 'otros_conceptos', 'fe_erratas', 'sociedad_unipersonal', 'declaracion_unipersonalidad', 'constitucion', 'suspension_pagos', '
perdida_caracter_unipersonalidad', 'cancelaciones_oficio_nombramientos', 'datos_registrales', 'cambio_domicilio_social', 'disolucion', 'ampliacion_objeto_social', 'cierre_provisional_hoj
a_registral_baja_en_el_indice_entidades_juridicas', 'ceses_dimisiones', 'nombramientos', 'situacion_concursal', 'modificaciones_estatutarias', 'ampliacion_capital', 'adaptacion_ley_2_95'
, 'cambio_denominacion_social', 'extincion', 'reduccion_capital', 'cambio_identidad_socio_unico', 'transformacion_sociedad', 'reapertura_hoja_registral', 'socio_unico', 'articulo_378_5
_reglamento_registro_mercantil', 'fusion_absorcion']
"""
