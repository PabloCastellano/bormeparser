#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# common.py - Common functions for bormeparser scripts
# Copyright (C) 2016 Pablo Castellano <pablo@anche.no>
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

DEFAULT_BORME_ROOT = '~/.bormes'

try:
    FileNotFoundError
except NameError:
    # Python 2
    FileNotFoundError = IOError


def get_borme_xml_filepath(date, directory):
    year = str(date.year)
    month = '{:02d}'.format(date.month)
    day = '{:02d}'.format(date.day)
    filename = 'BORME-S-{}{}{}.xml'.format(year, month, day)
    return os.path.join(os.path.expanduser(directory), 'xml', year, month, filename)


def get_borme_pdf_path(date, directory):
    year = str(date.year)
    month = '{:02d}'.format(date.month)
    day = '{:02d}'.format(date.day)
    return os.path.join(os.path.expanduser(directory), 'pdf', year, month, day)