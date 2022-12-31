#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# exceptions.py -
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



class BormeparserException(Exception):
    pass


class BormeIOErrorException(BormeparserException, IOError):
    pass


class BormeDoesntExistException(BormeparserException):
    pass


class BormeAlreadyDownloadedException(BormeparserException):
    pass


class BormeInvalidActoException(BormeparserException):
    pass


class BormeInvalidCargoException(BormeparserException):
    pass


class BormeAnuncioNotFound(BormeparserException):
    pass
