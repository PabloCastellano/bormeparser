#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# bormeparser.backends.parser1.parser.py -
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


from .functions import crop_file, clean_file, parse_file, parse_file_anuncios, convert_to_text_file

from bormeparser.backends.base import BormeAParserBackend

class Parser1(BormeAParserBackend):
    """
    Parse using pyPdf + pdfminer
    """
    def _parse(self):
        crop_file(self.filename, self.filename + '-cropped.pdf')
        convert_to_text_file(self.filename + '-cropped.pdf', self.filename + '.1.txt')
        clean_file(self.filename + '.1.txt', self.filename + '.2.txt')
        parse_file(self.filename + '.2.txt', self.filename + '.json')
        return True

    def _parse_actos(self, rewrite=True):
        crop_file(self.filename, self.filename + '-cropped.pdf', rewrite)
        convert_to_text_file(self.filename + '-cropped.pdf', self.filename + '.1.txt', rewrite)
        clean_file(self.filename + '.1.txt', self.filename + '.2.txt', rewrite)
        actos, _ = parse_file_anuncios(self.filename + '.2.txt', rewrite)
        return actos
