#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_acto.py -
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

import unittest

from bormeparser.acto import ACTO, ActoParser


class ActoTestCase(unittest.TestCase):

    def test_get_actoparser(self):
        parser_nombramientos = ACTO.get_parser('Nombramientos')
        parser_constitucion = ACTO.get_parser('Constitución')
        parser_ceses_dimisiones = ACTO.get_parser('Ceses/Dimisiones')
        parser_primera_inscripcion = ACTO.get_parser('Primera inscripcion (O.M. 10/6/1.997)')
        parser_cambio_objeto = ACTO.get_parser('Cambio de objeto social')

        self.assertEqual(parser_nombramientos, ActoParser.parse_nombramientos)
        self.assertEqual(parser_constitucion, ActoParser.parse_constitucion)
        self.assertEqual(parser_ceses_dimisiones, ActoParser.parse_ceses_dimisiones)
        self.assertEqual(parser_primera_inscripcion, ActoParser.parse_primera_inscripcion_o_m)
        self.assertEqual(parser_cambio_objeto, ActoParser.parse_default)


if __name__ == '__main__':
    unittest.main()
