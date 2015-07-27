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


def remove_accents(string):
    try:
        return ''.join((c for c in unicodedata.normalize('NFKD', string) if unicodedata.category(c) != 'Mn'))
    except TypeError:
        return ''.join((c for c in unicodedata.normalize('NFKD', unicode(string, 'utf-8')) if unicodedata.category(c) != 'Mn'))
