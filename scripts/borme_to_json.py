#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# borme_to_json.py - Convert BORME A PDF files to JSON
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

from bormeparser.backends.defaults import OPTIONS
OPTIONS['SANITIZE_COMPANY_NAME'] = True

import argparse
import logging
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert BORME A PDF files to JSON.')
    parser.add_argument('filename', help='BORME A PDF filename')
    parser.add_argument('--debug', action='store_true', default=False, help='Debug mode')
    parser.add_argument('-o', '--output', help='Output directory or filename (default is current directory)')
    args = parser.parse_args()

    # set logger DEBUG (Not working)
    if args.debug:
        bormeparser.borme.logger.setLevel(logging.DEBUG)
        bormeparser.backends.pypdf2.parser.logger.setLevel(logging.DEBUG)  # FIXME: DEFAULT_PARSER

    print('\nParsing {}'.format(args.filename))
    borme = bormeparser.parse(args.filename, bormeparser.SECCION.A)
    path = borme.to_json(args.output)

    if path:
        print('Created {}'.format(os.path.abspath(path)))
    else:
        print('Error creating JSON for {}'.format(args.filename))
