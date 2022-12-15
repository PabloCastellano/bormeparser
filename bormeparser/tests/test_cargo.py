#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_cargo.py -
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

import unittest

from bormeparser.cargo import CARGO
from bormeparser.exceptions import BormeInvalidCargoException


class CargoTestCase(unittest.TestCase):

    def test_from_string(self):
        self.assertEqual(CARGO.from_string('Adm.Man.Supl'), 'Administrador mancomunado suplente')
        self.assertEqual(CARGO.from_string('Vpr.Com.Ctr'), "Vicepresidente de la comisión de control")
        self.assertEqual(CARGO.from_string('V-PRE.COMS.C'), "Vicepresidente de la comisión de control")
        self.assertRaises(BormeInvalidCargoException, CARGO.from_string, 'Cargo invalido')


if __name__ == '__main__':
    unittest.main()
