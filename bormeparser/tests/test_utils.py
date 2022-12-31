#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_utils.py -
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

import datetime
import unittest

from bormeparser.utils import get_borme_website
from bormeparser.utils import acto_to_attr
from bormeparser.seccion import SECCION


class BormeparserUtilsTestCase(unittest.TestCase):

    def test_get_borme_website(self):
        date = datetime.date(2016, 4, 21)
        url = get_borme_website(date, SECCION.A)
        self.assertEqual(url, 'https://www.boe.es/borme/dias/2016/04/21/index.php?s=A')
        url = get_borme_website(date, SECCION.C)
        self.assertEqual(url, 'https://www.boe.es/borme/dias/2016/04/21/index.php?s=C')

    def test_acto_to_attr(self):
        attr1 = acto_to_attr('Nombramientos')
        attr2 = acto_to_attr('Ceses/Dimisiones')
        attr3 = acto_to_attr('Fusión por absorción')
        self.assertEqual(attr1, 'nombramientos')
        self.assertEqual(attr2, 'ceses_dimisiones')
        self.assertEqual(attr3, 'fusion_absorcion')


if __name__ == '__main__':
    unittest.main()
