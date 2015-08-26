#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_bormeregexp.py -
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

import unittest

from bormeparser.regex import regex_cargos, regex_empresa, is_company

DATA = {'fake1': {'Adm. Solid.': {'RAMA SANCHEZ JAVIER JORGE', 'RAMA SANCHEZ JOSE PEDRO'}},
        'fake2': {'Auditor': {'ACME AUDITORES SL'}, 'Aud.Supl.': {u'MACIAS MUÑOZ FELIPE JOSE'}},
        'fake3': {'Auditor': {'A.T.A AUDITORES SL'}, 'Aud.Supl.': {u'CUEVAS MUÑOZ SILVIA MARIA'}}}


class BormeparserIsCompanyTestCase(unittest.TestCase):
    empresa1 = 'PATATAS SL'
    empresa2 = 'HAMBURGUESAS AIE'
    empresa3 = 'ZANAHORIAS SA'
    empresa4 = 'COA-COA BARBACOA SRL'
    persona1 = 'JOHN DOE'

    def test_is_company(self):
        self.assertTrue(is_company(self.empresa1))
        self.assertTrue(is_company(self.empresa2))
        self.assertTrue(is_company(self.empresa3))
        self.assertTrue(is_company(self.empresa4))
        self.assertFalse(is_company(self.persona1))


class BormeparserRegexEmpresaTestCase(unittest.TestCase):
    acto1 = '57344 - ALDARA CATERING SL.'
    acto2 = '57344 - ALDARA CATERING SL'

    def test_regex_empresa(self):
        acto_id, empresa = regex_empresa(self.acto1)
        self.assertEqual(acto_id, 57344)
        self.assertEqual(empresa, 'ALDARA CATERING SL')

        acto_id, empresa = regex_empresa(self.acto1)
        self.assertEqual(acto_id, 57344)
        self.assertEqual(empresa, 'ALDARA CATERING SL')


class BormeparserRegexCargosTestCase(unittest.TestCase):
    nombramientos1 = 'Adm. Solid.: RAMA SANCHEZ JOSE PEDRO;RAMA SANCHEZ JAVIER JORGE.'
    nombramientos2 = u'Auditor: ACME AUDITORES SL. Aud.Supl.: MACIAS MUÑOZ FELIPE JOSE.'
    nombramientos3 = u'Auditor: A.T.A AUDITORES SL. Aud.Supl.: CUEVAS MUÑOZ SILVIA MARIA.'

    def test_regex_nombramientos(self):
        cargos1 = regex_cargos(self.nombramientos1)
        self.assertEqual(cargos1, DATA['fake1'])

        cargos2 = regex_cargos(self.nombramientos2)
        self.assertEqual(cargos2, DATA['fake2'])

        cargos3 = regex_cargos(self.nombramientos3)
        self.assertEqual(cargos3, DATA['fake3'])

if __name__ == '__main__':
    unittest.main()
