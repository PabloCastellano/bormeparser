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

from bormeparser.regex import regex_cargos, regex_empresa, regex_decl_unip, is_company, regex_escision, regex_fusion
from bormeparser.regex import is_acto_cargo_entrante, regex_empresa_tipo

DATA = {'fake1': {'Adm. Solid.': {'RAMA SANCHEZ JAVIER JORGE', 'RAMA SANCHEZ JOSE PEDRO'}},
        'fake2': {'Auditor': {'ACME AUDITORES SL'}, 'Aud.Supl.': {u'MACIAS MUÑOZ FELIPE JOSE'}},
        'fake3': {'Auditor': {'A.T.A AUDITORES SL'}, 'Aud.Supl.': {u'CUEVAS MUÑOZ SILVIA MARIA'}},
        'fake4': {'Adm. Mancom.': {'PEREZ', 'HILARIO'}},
        'fake5': {'Auditor': {'A.T.A AUDITORES SL'}, 'Adm. Mancom.': {'PEREZ', 'HILARIO'}},
        'fake6': {'Adm. Solid.': {'ASDFG INVERSIONES SL'}, 'Adm. Mancom.': {'ASDFG INVERSIONES SL', 'PEDRO PEREZ'}}}


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
    acto3 = u'473700 - SA COVA PLAÇA MAJOR SL(R.M. PALMA DE MALLORCA).'
    empresa1 = 'ALDARA CATERING SL'
    empresa2 = 'ALDARA CATERING'

    def test_regex_empresa(self):
        acto_id, empresa = regex_empresa(self.acto1)
        self.assertEqual(acto_id, 57344)
        self.assertEqual(empresa, 'ALDARA CATERING SL')

        acto_id, empresa = regex_empresa(self.acto2)
        self.assertEqual(acto_id, 57344)
        self.assertEqual(empresa, 'ALDARA CATERING SL')

        acto_id, empresa = regex_empresa(self.acto3)
        self.assertEqual(acto_id, 473700)
        self.assertEqual(empresa, u'SA COVA PLAÇA MAJOR SL')

    def test_regex_empresa_tipo(self):
        empresa, tipo = regex_empresa_tipo(self.empresa1)
        self.assertEqual(empresa, 'ALDARA CATERING')
        self.assertEqual(tipo, 'SL')

        empresa, tipo = regex_empresa_tipo(self.empresa2)
        self.assertEqual(empresa, 'ALDARA CATERING')
        self.assertEqual(tipo, '')


class BormeparserRegexCargosTestCase(unittest.TestCase):
    nombramientos1 = 'Adm. Solid.: RAMA SANCHEZ JOSE PEDRO;RAMA SANCHEZ JAVIER JORGE.'
    nombramientos2 = u'Auditor: ACME AUDITORES SL. Aud.Supl.: MACIAS MUÑOZ FELIPE JOSE.'
    nombramientos3 = u'Auditor: A.T.A AUDITORES SL. Aud.Supl.: CUEVAS MUÑOZ SILVIA MARIA.'
    nombramientos4 = u'Adm. Solid.: ASDFG INVERSIONES S.L. Adm. Mancom.: ASDFG INVERSIONES S.L.;PEDRO PEREZ'
    ceses1 = u'Adm. Mancom.: PEREZ;HILARIO'
    ceses2 = u'Auditor: A.T.A AUDITORES SL. Adm. Mancom.: PEREZ;HILARIO'

    def test_regex_nombramientos(self):
        cargos1 = regex_cargos(self.nombramientos1)
        self.assertEqual(cargos1, DATA['fake1'])

        cargos2 = regex_cargos(self.nombramientos2)
        self.assertEqual(cargos2, DATA['fake2'])

        cargos3 = regex_cargos(self.nombramientos3)
        self.assertEqual(cargos3, DATA['fake3'])

        cargos4 = regex_cargos(self.nombramientos4)
        self.assertEqual(cargos4, DATA['fake6'])

        ceses1 = regex_cargos(self.ceses1)
        self.assertEqual(ceses1, DATA['fake4'])

        ceses2 = regex_cargos(self.ceses2)
        self.assertEqual(ceses2, DATA['fake5'])

    def test_cargo_entrante(self):
        self.assertTrue(is_acto_cargo_entrante('Reelecciones'))
        self.assertTrue(is_acto_cargo_entrante('Nombramientos'))
        self.assertFalse(is_acto_cargo_entrante('Ceses/Dimisiones'))
        self.assertRaises(ValueError, is_acto_cargo_entrante, 'Cambio de domicilio social')


class BormeparserRegexRareTestCase(unittest.TestCase):
    string1 = u'Declaración de unipersonalidad. Socio único: GRUPO DE EMPRESAS E INVERSIONES YOLO S.L. Nombramientos'
    string2 = u'Declaración de unipersonalidad. Socio único: JOHN DOE. Datos registrales'
    string3 = u'Declaración de unipersonalidad. Socio único: FOO DOE. Pérdida del caracter de unipersonalidad. Cambio de domicilio social.'
    string7 = u'Declaración de unipersonalidad. Socio único: CORPOREISHON BLA BLA. Cif:B12345678.Ceses/Dimisiones.'

    string4 = u'Sociedades beneficiarias de la escisión: PEPE SL.'
    string5 = u'PEDRO ANTONIO 2001 SOCIEDAD LIMITADA. PEDRO ANTONIO EXPLOTACIONES SL.'
    string6 = u'Sociedades que se fusiónan: YOLO SOCIEDAD ANONIMA.'

    def test_regex_decl_unip(self):
        acto_colon, arg_colon, nombreacto = regex_decl_unip(self.string1)
        self.assertEqual(acto_colon, u'Declaración de unipersonalidad')
        self.assertEqual(arg_colon, {u'Socio Único': {'GRUPO DE EMPRESAS E INVERSIONES YOLO S.L'}})
        self.assertEqual(nombreacto, 'Nombramientos')

        acto_colon, arg_colon, nombreacto = regex_decl_unip(self.string2)
        self.assertEqual(acto_colon, u'Declaración de unipersonalidad')
        self.assertEqual(arg_colon, {u'Socio Único': {'JOHN DOE'}})
        self.assertEqual(nombreacto, 'Datos registrales')

        acto_colon, arg_colon, nombreacto = regex_decl_unip(self.string3)
        self.assertEqual(acto_colon, u'Declaración de unipersonalidad')
        self.assertEqual(arg_colon, {u'Socio Único': {'FOO DOE'}})
        self.assertEqual(nombreacto, u'Pérdida del caracter de unipersonalidad. Cambio de domicilio social.')

        acto_colon, arg_colon, nombreacto = regex_decl_unip(self.string7)
        self.assertEqual(acto_colon, u'Declaración de unipersonalidad')
        self.assertEqual(arg_colon, {u'Socio Único': {'CORPOREISHON BLA BLA. Cif:B12345678'}})
        self.assertEqual(nombreacto, u'Ceses/Dimisiones.')

    def test_regex_escision(self):
        nombreacto, beneficiarias = regex_escision(u'Escisión parcial', self.string4)
        self.assertEqual(nombreacto, u'Escisión parcial')
        self.assertEqual(beneficiarias, {'Sociedades beneficiarias': {'PEPE SL'}})

        nombreacto, beneficiarias = regex_escision(u'Escisión total. Sociedades beneficiarias de la escisión', self.string5)
        self.assertEqual(nombreacto, u'Escisión total')
        self.assertEqual(beneficiarias, {'Sociedades beneficiarias': {'PEDRO ANTONIO 2001 SOCIEDAD LIMITADA', 'PEDRO ANTONIO EXPLOTACIONES SL'}})

    def test_regex_fusion(self):
        sociedad = regex_fusion(self.string6)
        self.assertEqual(sociedad, {'Sociedades fusionadas': {'YOLO SOCIEDAD ANONIMA'}})


if __name__ == '__main__':
    unittest.main()
