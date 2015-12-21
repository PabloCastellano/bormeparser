#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# bormeparser.backends.pypdf2.parser.py -
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


#from __future__ import absolute_import
#from functions import parse_file
from .functions import parse_file, logger
from bormeparser.backends.base import BormeParserBackend
import logging


class PyPDF2Parser(BormeParserBackend):
    """
    Parse using PyPDF2
    """
    def __init__(self, filename, log_level=logging.WARN):
        super(PyPDF2Parser, self).__init__(filename)
        logger.setLevel(log_level)

    def _parse(self):
        return parse_file(self.filename)


if __name__ == '__main__':
    import pprint
    actos = parse_file('../../../pdf/BORME-A-2015-27-10.pdf')
    pprint.pprint(actos, width=160)
