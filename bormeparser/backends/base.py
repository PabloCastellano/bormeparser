#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# bormeparser.backends.base.py -
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


import os

from bormeparser.borme import Borme, BormeAnuncio
from bormeparser.regex import regex_fecha
from bormeparser import SECCION, PROVINCIA


class BormeParserBackend(object):
    def __init__(self, filename):

        if not os.path.isfile(filename):
            raise IOError

        self.filename = filename

    def parse(self):
        anuncios = self._parse()
        bormeanuncios = []
        for id_anuncio in anuncios.keys():
            if not isinstance(id_anuncio, int):
                continue
            data = anuncios[id_anuncio]
            a = BormeAnuncio(id_anuncio, data['Empresa'], data['Actos'])
            bormeanuncios.append(a)

        fecha = regex_fecha(anuncios['borme_fecha'])
        seccion = SECCION.from_borme(anuncios['borme_seccion'], anuncios['borme_subseccion'])
        provincia = PROVINCIA.from_title(anuncios['borme_provincia'])
        return Borme(fecha, seccion, provincia, anuncios['borme_num'], anuncios['borme_cve'], bormeanuncios, filename=self.filename)

    def _parse(self):
        """
        :return: diccionario con key= id del acto y value {'Empresa': str, 'Actos': dict}
        """
        raise NotImplementedError

    def parse_actos(self):
        self._parse_actos()

    def _parse_actos(self):
        raise NotImplementedError
