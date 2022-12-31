#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# seccion.py -
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


class SECCION:
    A = 'A'
    B = 'B'
    C = 'C'

    # TODO: No detecta tipo C, viene el texto comprimido
    @staticmethod
    def from_borme(seccion, subseccion):
        if 'SECCIÓN PRIMERA' in seccion:
            if subseccion == 'Actos inscritos':
                return SECCION.A
            elif subseccion == 'Otros actos publicados en el Registro Mercantil':
                return SECCION.B
            else:
                raise ValueError('InvalidSeccion: %s %s' % (seccion, subseccion))
        else:
            raise ValueError('InvalidSeccion: %s %s' % (seccion, subseccion))


class SUBSECCION:
    # SECCIÓN PRIMERA. Empresarios.
    # Actos inscritos
    ACTOS_INSCRITOS = 'A'
    # SECCIÓN PRIMERA. Empresarios.
    # Otros actos publicados en el Registro Mercantil
    OTROS_ACTOS = 'B'
    # SECCIÓN SEGUNDA. Anuncios y avisos legales
    ANUNCIOS_Y_AVISOS_LEGALES = 'C'
