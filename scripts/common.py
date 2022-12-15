#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# common.py - Common functions for bormeparser scripts
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

import os
import subprocess


def get_git_revision_short_hash():
    try:
        version = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip()
        if isinstance(version, bytes):
            version = version.decode('unicode_escape')
    except subprocess.CalledProcessError:
        version = 'Unknown'
    return version
