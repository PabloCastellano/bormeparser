#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# debug_content_pdf.py - Debug PDF content
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

import argparse

from PyPDF2 import PdfFileReader


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Debug PDF content.')
    parser.add_argument('filename', help='BORME A PDF filename')
    args = parser.parse_args()

    reader = PdfFileReader(open(args.filename, 'rb'))
    for n in range(0, reader.getNumPages()):
        content = reader.getPage(n).getContents().getData()

        # Python 3
        if isinstance(content, bytes):
            content = content.decode('unicode_escape')

        #print(content)
        for line in content.split('\n'):
            print(line)
