#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_borme.py -
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

import datetime
import tempfile
import unittest

from bormeparser.borme import Borme, BormeActoCargo, BormeActoTexto, BormeAnuncio
from bormeparser.seccion import SECCION
from bormeparser.provincia import PROVINCIA


DATA1 = {214: {'Actos': {'Ceses/Dimisiones': {'Adm. Unico': {'JUAN GARCIA GARCIA'}},
                         'Datos registrales': 'T 5188, L 4095, F 146, S 8, H MA120039, I/A 4 (25.05.15).',
                         'Constitución': 'Comienzo de operaciones: 1.04.15. Objeto social: blabla. Domicilio: C/ RANDOM 1 2 (MALAGA). Capital: 3.000,00 Euros.',
                         'Nombramientos': {'Adm. Unico': {'PEDRO GOMEZ GOMEZ'}}},
               'Empresa': 'EMPRESA RANDOM SL.'},
         'borme_cve': 'BORME-A-2015-102-29',
         'borme_fecha': 'Martes 2 de junio de 2015',
         'borme_num': 102,
         'borme_provincia': 'MÁLAGA',
         'borme_seccion': 'SECCIÓN PRIMERA'
         }


class BormeTestCase(unittest.TestCase):
    def setUp(self):
        bormeanuncios = [BormeAnuncio(1, DATA1[214]['Empresa'], DATA1[214]['Actos'])]
        self.borme = Borme((2015, 2, 10), 'A', PROVINCIA.CACERES, 27, 'BORME-A-2015-27-10', bormeanuncios)

    def test_instance(self):
        self.assertEqual(self.borme.date, datetime.date(year=2015, month=2, day=10))
        self.assertEqual(self.borme.seccion, SECCION.A)
        self.assertEqual(self.borme.provincia, PROVINCIA.CACERES)
        self.assertEqual(self.borme.num, 27)
        self.assertEqual(self.borme.cve, 'BORME-A-2015-27-10')
        self.assertEqual(self.borme.url, 'http://boe.es/borme/dias/2015/02/10/pdfs/BORME-A-2015-27-10.pdf')
        self.assertEqual(self.borme.filename, None)

    def test_to_json(self):
        fp = tempfile.NamedTemporaryFile()
        converted = self.borme.to_json(fp.name)
        self.assertTrue(converted)
        fp.close()


class BormeAnuncioTestCase(unittest.TestCase):
    def setUp(self):
        self.anuncio = BormeAnuncio(1, DATA1[214]['Empresa'], DATA1[214]['Actos'])

    def test_instance(self):
        self.assertEqual(self.anuncio.id, 1)
        self.assertEqual(self.anuncio.empresa, DATA1[214]['Empresa'])
        self.assertEqual(self.anuncio.datos_registrales, DATA1[214]['Actos']['Datos registrales'])

    def test_get_actos(self):
        actos = list(self.anuncio.get_actos())
        actos.sort()  # Sort dictionary
        self.assertEqual(len(actos), 3)
        self.assertEqual(actos[0], ('Ceses/Dimisiones', DATA1[214]['Actos']['Ceses/Dimisiones']))
        self.assertEqual(actos[1], ('Constitución', DATA1[214]['Actos']['Constitución']))
        self.assertEqual(actos[2], ('Nombramientos', DATA1[214]['Actos']['Nombramientos']))

    def test_get_borme_actos(self):
        actos = self.anuncio.get_borme_actos()
        actos.sort()  # Sort dictionary
        self.assertEqual(len(actos), 3)
        self.assertIsInstance(actos[0], BormeActoCargo)
        self.assertEqual(actos[0].name, 'Ceses/Dimisiones')
        self.assertEqual(actos[0].cargos, DATA1[214]['Actos']['Ceses/Dimisiones'])
        self.assertIsInstance(actos[1], BormeActoTexto)
        self.assertEqual(actos[1].name, 'Constitución')
        self.assertEqual(actos[1].value, DATA1[214]['Actos']['Constitución'])
        self.assertIsInstance(actos[2], BormeActoCargo)
        self.assertEqual(actos[2].name, 'Nombramientos')
        self.assertEqual(actos[2].cargos, DATA1[214]['Actos']['Nombramientos'])


class BormeActoTestCase(unittest.TestCase):
    def test_cargo_instance(self):
        acto = BormeActoCargo('Nombramientos', DATA1[214]['Actos']['Nombramientos'])
        self.assertEqual(len(acto.cargos), 1)
        self.assertEqual(acto.cargos['Adm. Unico'], DATA1[214]['Actos']['Nombramientos']['Adm. Unico'])

        # Exceptions
        self.assertRaises(ValueError, BormeActoCargo, 'Acto invalido', 'mal')
        self.assertRaises(ValueError, BormeActoCargo, 'Constitución', 'mal')
        self.assertRaises(ValueError, BormeActoCargo, 'Nombramientos', 'mal')

    def test_texto_instance(self):
        acto = BormeActoTexto('Constitución', DATA1[214]['Actos']['Constitución'])
        self.assertEqual(acto.value, DATA1[214]['Actos']['Constitución'])

        # Exceptions
        self.assertRaises(ValueError, BormeActoTexto, 'Acto invalido', ['mal'])
        self.assertRaises(ValueError, BormeActoTexto, 'Nombramientos', ['mal'])


if __name__ == '__main__':
    unittest.main()
