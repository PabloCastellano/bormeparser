#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# parser.py -
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


import importlib
import os

try:
    # Python 3
    from urllib import request
except ImportError:
    import urllib as request

# backends
DEFAULT_PARSER = ('bormeparser.backends.pypdf2.parser', 'PyPDF2Parser')


# parse: url, filename (string)
def parse(data):
    module = importlib.import_module(DEFAULT_PARSER[0])
    parser = getattr(module, DEFAULT_PARSER[1])
    if os.path.isfile(data):
        borme = parser(data).parse()
    elif data.startswith('http'):
        # TODO
        #content = request.urlopen(data).read()
        borme = parser(data).parse()
    else:
        raise FileNotFoundError(data)

    return borme
