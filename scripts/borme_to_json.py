#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# borme_to_json.py -
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
import os
import sys


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} <filename.pdf> [--debug]'.format(sys.argv[0]))
        sys.exit(1)

    # set logger DEBUG (Not working)
    if len(sys.argv) == 3 and sys.argv[2] == '--debug':
        bormeparser.borme.logger.setLevel(logging.DEBUG)
        bormeparser.backends.pypdf2.functions.logger.setLevel(logging.DEBUG)  # FIXME: DEFAULT_PARSER

    # filename
    filename = os.path.basename(sys.argv[1]).replace('.pdf', '.json')
    borme = bormeparser.parse(sys.argv[1], bormeparser.SECCION.A)
    borme.to_json(filename)

    print()
    print('Created %s' % os.path.abspath(filename))
