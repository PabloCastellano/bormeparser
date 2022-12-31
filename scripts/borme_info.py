#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# borme_info.py - Shows BORME A info
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

import bormeparser
import bormeparser.backends.pypdf2.parser
from bormeparser.exceptions import BormeAnuncioNotFound

import argparse
import logging
import sys


def print_anuncio(anuncio):
    print('\nAnuncio {}'.format(anuncio.id))
    print('-' * (8 + len(str(anuncio.id))))
    print()
    for acto, valor in anuncio.get_actos():
        print('  {}'.format(acto))
        print('    {}'.format(valor))
    print('  Datos registrales')
    print('    ' + anuncio.datos_registrales)
    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Shows BORME A info.')
    parser.add_argument('filename', help='BORME A PDF filename')
    parser.add_argument('-n', '--number', nargs='*', type=int, help='Show Verbose mode')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Verbose mode')
    args = parser.parse_args()

    # set logger DEBUG (Not working)
    if args.verbose:
        bormeparser.borme.logger.setLevel(logging.DEBUG)
        bormeparser.backends.pypdf2.parser.logger.setLevel(logging.DEBUG)  # FIXME: DEFAULT_PARSER

    borme = bormeparser.parse(args.filename, bormeparser.SECCION.A)

    if args.number:
        anuncios = []
        for n in args.number:
            try:
                anuncio = borme.get_anuncio(n)
                anuncios.append(anuncio)
            except BormeAnuncioNotFound:
                print('No existe el anuncio {}. Elije uno entre {} y {}.'.format(n, borme.anuncios_rango[0], borme.anuncios_rango[1]))
                sys.exit(1)
    else:
        anuncios = borme.get_anuncios()

    for anuncio in anuncios:
        print_anuncio(anuncio)

    if not args.number:
        print('Otros datos')
        print('-----\n')
        print('  CVE: {}'.format(borme.cve))
        print('  Fecha: {}'.format(borme.date))
        print('  Num: {}'.format(borme.num))
        print('  Provincia: {}'.format(borme.provincia))
        print('  Seccion: {}'.format(borme.seccion))
        print('  Anuncios incluidos: {}'.format(len(borme.get_anuncios())))
