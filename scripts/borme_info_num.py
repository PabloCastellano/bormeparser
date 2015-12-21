#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# borme_info_num.py -
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
import bormeparser.borme
import bormeparser.backends.pypdf2.functions
from bormeparser.exceptions import BormeAnuncioNotFound
import logging
import sys


# TODO: Fusionar con borme_info.py
# file.pdf 233232 [--debug]
# file.pdf 223234,223243,223244,223250,223253,223254 [--debug]
if __name__ == '__main__':

    # set logger DEBUG
    if len(sys.argv) == 4 and sys.argv[3] == '--debug':
        bormeparser.borme.logger.setLevel(logging.DEBUG)
        bormeparser.backends.pypdf2.functions.logger.setLevel(logging.DEBUG)  # FIXME: DEFAULT_PARSER

    borme = bormeparser.parse(sys.argv[1])

    for id in sys.argv[2].split(','):
        try:
            anuncio = borme.get_anuncio(int(id))
            print('Anuncio %d' % anuncio.id)
            print('-' * (8 + len(str(anuncio.id))))
            print()
            for acto, valor in anuncio.get_actos():
                print('  %s' % acto)
                print('    %s' % valor)
            print('  Datos registrales')
            print('    %s' % anuncio.datos_registrales)
        except BormeAnuncioNotFound:
            print('No existe el anuncio %s' % id)
        print()
