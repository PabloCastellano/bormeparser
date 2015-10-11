#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# utils.py -
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

import unicodedata
import datetime

FIRST_BORME = {2009: datetime.date(2009, 1, 2),
               2010: datetime.date(2010, 1, 4),
               2011: datetime.date(2011, 1, 3),
               2012: datetime.date(2012, 1, 2),
               2013: datetime.date(2013, 1, 2),
               2014: datetime.date(2014, 1, 2),
               2015: datetime.date(2015, 1, 2)}


def remove_accents(string):
    try:
        return ''.join((c for c in unicodedata.normalize('NFKD', string) if unicodedata.category(c) != 'Mn'))
    except TypeError:
        return ''.join((c for c in unicodedata.normalize('NFKD', unicode(string, 'utf-8')) if unicodedata.category(c) != 'Mn'))
