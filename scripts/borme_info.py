#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# borme_info.py -
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


import bormeparser
import bormeparser.backends.pypdf2.functions
import logging
import sys


# TODO: Fusionar con borme_info_num.py

if __name__ == '__main__':

    # set logger DEBUG (Not working)
    if len(sys.argv) == 3 and sys.argv[2] == '--debug':
        bormeparser.borme.logger.setLevel(logging.DEBUG)
        bormeparser.backends.pypdf2.functions.logger.setLevel(logging.DEBUG)  # FIXME: DEFAULT_PARSER

    borme = bormeparser.parse(sys.argv[1])

    for anuncio in borme.get_anuncios():
        print('Anuncio %d' % anuncio.id)
        print('-' * (8 + len(str(anuncio.id))))
        print()
        for acto, valor in anuncio.get_actos():
            print('  %s' % acto)
            print('    %s' % valor)
        print('  Datos registrales')
        print('    %s' % anuncio.datos_registrales)
        print()

    print('Otros')
    print('-----')
    print()
    print('  CVE: %s' % borme.cve)
    print('  Fecha: %s' % borme.date)
    print('  Num: %s' % borme.num)
    print('  Provincia: %s' % borme.provincia)
    print('  Seccion: %s' % borme.seccion)
    print('  Anuncios incluidos: %d' % len(borme.get_anuncios()))
