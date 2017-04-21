#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# provincia.py -
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

from bormeparser.utils import remove_accents

class Provincia:
    def __init__(self, name, code):
        self.name = name
        self._code = code

    @property
    def code(self):
        return '%02d' % self._code

    def __str__(self):
        return self.name

    def __repr__(self):
        return '%s: %s' % (self.__class__, self.name)

    def __lt__(self, other):
        return self.name < other.name

    # TODO: tildes
    def __eq__(self, other):
        """ Hace posible comparar la clase con una cadena (nombre de provincia) """
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        elif isinstance(other, str):
            return self.name.upper() == other.upper()
        else:
            return False

    def __hash__(self):
        return hash((self.name, self._code))


class PROVINCIA:
    ALAVA = Provincia('Álava', 1)
    ARABA = ALAVA
    ALBACETE = Provincia('Albacete', 2)
    ALICANTE = Provincia('Alicante', 3)
    ALMERIA = Provincia('Almería', 4)
    AVILA = Provincia('Ávila', 5)
    BADAJOZ = Provincia('Badajoz', 6)
    ISLAS_BALEARES = Provincia('Islas Baleares', 7)
    ILLES_BALEARS = ISLAS_BALEARES
    BARCELONA = Provincia('Barcelona', 8)
    BURGOS = Provincia('Burgos', 9)
    CACERES = Provincia('Cáceres', 10)
    CADIZ = Provincia('Cádiz', 11)
    CASTELLON = Provincia('Castellón', 12)
    CIUDAD_REAL = Provincia('Ciudad Real', 13)
    CORDOBA = Provincia('Córdoba', 14)
    LA_CORUNA = Provincia('La Coruña', 15)
    A_CORUNA = LA_CORUNA
    CUENCA = Provincia('Cuenca', 16)
    GERONA = Provincia('Gerona', 17)
    GIRONA = GERONA
    GRANADA = Provincia('Granada', 18)
    GUADALAJARA = Provincia('Guadalajara', 19)
    GUIPUZCOA = Provincia('Guipúzcoa', 20)
    GIPUZKOA = GUIPUZCOA
    HUELVA = Provincia('Huelva', 21)
    HUESCA = Provincia('Huesca', 22)
    JAEN = Provincia('Jaén', 23)
    LEON = Provincia('León', 24)
    LERIDA = Provincia('Lérida', 25)
    LLEIDA = LERIDA
    LA_RIOJA = Provincia('La Rioja', 26)
    LUGO = Provincia('Lugo', 27)
    MADRID = Provincia('Madrid', 28)
    MALAGA = Provincia('Málaga', 29)
    MURCIA = Provincia('Murcia', 30)
    NAVARRA = Provincia('Navarra', 31)
    ORENSE = Provincia('Orense', 32)
    OURENSE = ORENSE
    ASTURIAS = Provincia('Asturias', 33)
    PALENCIA = Provincia('Palencia', 34)
    LAS_PALMAS = Provincia('Las Palmas', 35)
    PONTEVEDRA = Provincia('Pontevedra', 36)
    SALAMANCA = Provincia('Salamanca', 37)
    SANTA_CRUZ_DE_TENERIFE = Provincia('Santa Cruz de Tenerife', 38)
    CANTABRIA = Provincia('Cantabria', 39)
    SEGOVIA = Provincia('Segovia', 40)
    SEVILLA = Provincia('Sevilla', 41)
    SORIA = Provincia('Soria', 42)
    TARRAGONA = Provincia('Tarragona', 43)
    TERUEL = Provincia('Teruel', 44)
    TOLEDO = Provincia('Toledo', 45)
    VALENCIA = Provincia('Valencia', 46)
    VALLADOLID = Provincia('Valladolid', 47)
    VIZCAYA = Provincia('Vizcaya', 48)
    BIZKAIA = VIZCAYA
    ZAMORA = Provincia('Zamora', 49)
    ZARAGOZA = Provincia('Zaragoza', 50)
    CEUTA = Provincia('Ceuta', 51)
    MELILLA = Provincia('Melilla', 52)

    @staticmethod
    def from_title(title):
        try:
            if title == 'ARABA/ÁLAVA':
                return PROVINCIA.ALAVA
            title = remove_accents(title).replace(' ', '_')
            return getattr(PROVINCIA, title)
        except AttributeError:
            raise ValueError('InvalidProvince: %s' % title)

ALL_PROVINCIAS = list(filter(lambda x: not x.startswith('__') and x != 'from_title', vars(PROVINCIA)))
