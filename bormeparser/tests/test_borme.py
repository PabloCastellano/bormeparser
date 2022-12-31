#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_borme.py -
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
import json
import os
import tempfile
import unittest

import bormeparser
from bormeparser.borme import (
        Borme, BormeActoCargo, BormeActoTexto, BormeAnuncio, BormeXML)
from bormeparser.exceptions import BormeDoesntExistException
from bormeparser.seccion import SECCION
from bormeparser.provincia import PROVINCIA

EXAMPLES_PATH = os.path.join(os.path.dirname(bormeparser.__file__),
                             '..',
                             'examples')

DATA1 = {
    214: {
        'Actos': [
            {'Ceses/Dimisiones': {'Adm. Unico': {'JUAN GARCIA GARCIA'}}},
            {'Datos registrales': 'T 5188, L 4095, F 146, S 8, H MA120039, I/A 4 (25.05.15).'},
            {'Constitución': 'Comienzo de operaciones: 1.04.15. Objeto social: blabla. Domicilio: C/ RANDOM 1 2 (MALAGA). Capital: 3.000,00 Euros.'},
            {'Nombramientos': {'Adm. Unico': {'PEDRO GOMEZ GOMEZ'}}}],
        'Extra': {
            "liquidacion": False, "sucursal": False, "registro": "R.M. MAHON"},
        'Empresa': 'EMPRESA RANDOM SL.'
        },
    'borme_cve': 'BORME-A-2015-102-29',
    'borme_fecha': 'Martes 2 de junio de 2015',
    'borme_num': 102,
    'borme_provincia': 'MÁLAGA',
    'borme_seccion': 'SECCIÓN PRIMERA'
}


class BormeATestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.borme = bormeparser.parse(
            os.path.join(EXAMPLES_PATH, 'BORME-A-2015-27-10.pdf'), SECCION.A)

    def test_instance(self):
        self.assertEqual(self.borme.date, datetime.date(year=2015, month=2, day=10))
        self.assertEqual(self.borme.seccion, SECCION.A)
        self.assertEqual(self.borme.provincia, PROVINCIA.CACERES)
        self.assertEqual(self.borme.num, 27)
        self.assertEqual(self.borme.cve, 'BORME-A-2015-27-10')
        self.assertEqual(self.borme.url, 'https://boe.es/borme/dias/2015/02/10/pdfs/BORME-A-2015-27-10.pdf')
        self.assertEqual(self.borme.filename, os.path.join(EXAMPLES_PATH, 'BORME-A-2015-27-10.pdf'))

    def test_get_anuncios_ids(self):
        ids = self.borme.get_anuncios_ids()
        self.assertEqual(ids, list(range(57315, 57345)))

    def test_json(self):
        temp_fp = tempfile.NamedTemporaryFile()
        temp_filename = temp_fp.name

        converted = self.borme.to_json(temp_filename)
        self.assertTrue(converted)

        # Check output json values
        with open(temp_filename) as fp:
            data = json.load(fp)

        self.assertEqual(data['cve'], 'BORME-A-2015-27-10')
        self.assertEqual(data['date'], '2015-02-10')
        self.assertEqual(data['seccion'], 'A')
        self.assertEqual(data['provincia'], 'Cáceres')
        self.assertEqual(data['num'], 27)
        self.assertEqual(data['url'], 'https://boe.es/borme/dias/2015/02/10/pdfs/BORME-A-2015-27-10.pdf')
        self.assertEqual(data['from_anuncio'], 57315)
        self.assertEqual(data['to_anuncio'], 57344)
        self.assertEqual(data['num_anuncios'], 30)

        # Borme.from_json(): use filename as parameter
        b = Borme.from_json(temp_filename)

        self.assertEqual(b.date, datetime.date(year=2015, month=2, day=10))
        self.assertEqual(b.seccion, SECCION.A)
        self.assertEqual(b.provincia, PROVINCIA.CACERES)
        self.assertEqual(b.num, 27)
        self.assertEqual(b.cve, 'BORME-A-2015-27-10')
        self.assertEqual(b.url, 'https://boe.es/borme/dias/2015/02/10/pdfs/BORME-A-2015-27-10.pdf')
        self.assertEqual(b.filename, temp_filename)

        # Borme.from_json(): use file object as parameter
        with open(temp_filename) as fp:
            b = Borme.from_json(fp)

        self.assertEqual(b.date, datetime.date(year=2015, month=2, day=10))
        self.assertEqual(b.seccion, SECCION.A)
        self.assertEqual(b.provincia, PROVINCIA.CACERES)
        self.assertEqual(b.num, 27)
        self.assertEqual(b.cve, 'BORME-A-2015-27-10')
        self.assertEqual(b.url, 'https://boe.es/borme/dias/2015/02/10/pdfs/BORME-A-2015-27-10.pdf')
        self.assertEqual(b.filename, temp_filename)

        temp_fp.close()


class FakeBormeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bormeanuncios = [BormeAnuncio(1, DATA1[214]['Empresa'], DATA1[214]['Actos'], DATA1[214]['Extra'])]
        cls.borme = Borme((2015, 2, 10), 'A', PROVINCIA.CACERES, 27, 'BORME-A-2015-27-10', bormeanuncios)

    def test_instance(self):
        self.assertEqual(self.borme.date, datetime.date(year=2015, month=2, day=10))
        self.assertEqual(self.borme.seccion, SECCION.A)
        self.assertEqual(self.borme.provincia, PROVINCIA.CACERES)
        self.assertEqual(self.borme.num, 27)
        self.assertEqual(self.borme.cve, 'BORME-A-2015-27-10')
        self.assertEqual(self.borme.url, 'https://boe.es/borme/dias/2015/02/10/pdfs/BORME-A-2015-27-10.pdf')
        self.assertEqual(self.borme.filename, None)

    def test_to_json(self):
        fp = tempfile.NamedTemporaryFile()
        filename = fp.name
        fp.close()
        converted = self.borme.to_json(filename)
        self.assertTrue(converted)

        fp = open(filename)
        data = json.load(fp)
        fp.close()

        self.assertEqual(data['cve'], 'BORME-A-2015-27-10')
        self.assertEqual(data['date'], '2015-02-10')
        self.assertEqual(data['seccion'], 'A')
        self.assertEqual(data['provincia'], 'Cáceres')
        self.assertEqual(data['num'], 27)
        self.assertEqual(data['url'], 'https://boe.es/borme/dias/2015/02/10/pdfs/BORME-A-2015-27-10.pdf')
        self.assertEqual(data['from_anuncio'], 1)
        self.assertEqual(data['to_anuncio'], 1)
        self.assertEqual(data['num_anuncios'], 1)


class BormeAnuncioTestCase(unittest.TestCase):
    def setUp(self):
        self.anuncio = BormeAnuncio(1, DATA1[214]['Empresa'], DATA1[214]['Actos'], DATA1[214]['Extra'])

    def test_instance(self):
        self.assertEqual(self.anuncio.id, 1)
        self.assertEqual(self.anuncio.empresa, DATA1[214]['Empresa'])
        self.assertEqual(self.anuncio.registro, DATA1[214]['Extra']["registro"])
        self.assertEqual(self.anuncio.sucursal, DATA1[214]['Extra']["sucursal"])
        self.assertEqual(self.anuncio.liquidacion, DATA1[214]['Extra']["liquidacion"])
        self.assertEqual(self.anuncio.datos_registrales, DATA1[214]['Actos'][1]['Datos registrales'])

    def test_get_actos(self):
        actos = list(self.anuncio.get_actos())
        actos.sort()  # Sort dictionary
        self.assertEqual(len(actos), 3)
        self.assertEqual(actos[0], ('Ceses/Dimisiones', DATA1[214]['Actos'][0]['Ceses/Dimisiones']))
        self.assertEqual(actos[1], ('Constitución', DATA1[214]['Actos'][2]['Constitución']))
        self.assertEqual(actos[2], ('Nombramientos', DATA1[214]['Actos'][3]['Nombramientos']))

    def test_get_borme_actos(self):
        actos = self.anuncio.get_borme_actos()
        actos.sort()  # Sort dictionary
        self.assertEqual(len(actos), 3)
        self.assertIsInstance(actos[0], BormeActoCargo)
        self.assertEqual(actos[0].name, 'Ceses/Dimisiones')
        self.assertEqual(actos[0].cargos, DATA1[214]['Actos'][0]['Ceses/Dimisiones'])
        self.assertIsInstance(actos[1], BormeActoTexto)
        self.assertEqual(actos[1].name, 'Constitución')
        self.assertEqual(actos[1].value, DATA1[214]['Actos'][2]['Constitución'])
        self.assertIsInstance(actos[2], BormeActoCargo)
        self.assertEqual(actos[2].name, 'Nombramientos')
        self.assertEqual(actos[2].cargos, DATA1[214]['Actos'][3]['Nombramientos'])


class BormeActoTestCase(unittest.TestCase):
    def test_cargo_instance(self):
        acto = BormeActoCargo('Nombramientos', DATA1[214]['Actos'][3]['Nombramientos'])
        self.assertEqual(len(acto.cargos), 1)
        self.assertEqual(acto.cargos['Adm. Unico'], DATA1[214]['Actos'][3]['Nombramientos']['Adm. Unico'])

        # Exceptions
        self.assertRaises(ValueError, BormeActoCargo, 'Acto invalido', 'mal')
        self.assertRaises(ValueError, BormeActoCargo, 'Constitución', 'mal')
        self.assertRaises(ValueError, BormeActoCargo, 'Nombramientos', 'mal')

    def test_texto_instance(self):
        acto = BormeActoTexto('Constitución', DATA1[214]['Actos'][2]['Constitución'])
        self.assertEqual(acto.value, DATA1[214]['Actos'][2]['Constitución'])

        # Exceptions
        self.assertRaises(ValueError, BormeActoTexto, 'Acto invalido', ['mal'])
        self.assertRaises(ValueError, BormeActoTexto, 'Nombramientos', ['mal'])


class BormeXMLInstanceTestCase(unittest.TestCase):
    date = (2015, 9, 24)
    url = 'https://www.boe.es/diario_borme/xml.php?id=BORME-S-20150924'
    url_insecure = 'http://www.boe.es/diario_borme/xml.php?id=BORME-S-20150924'
    nbo = 183

    def test_from_file(self):
        path = os.path.join(EXAMPLES_PATH, 'BORME-S-20150924.xml')

        # from local file
        bxml = BormeXML.from_file(path)
        self.assertEqual(bxml.url, self.url)
        self.assertEqual(bxml.date, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2]))
        self.assertEqual(bxml.filename, path)
        self.assertEqual(bxml.nbo, self.nbo)
        self.assertEqual(bxml.prev_borme, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2] - 1))
        self.assertEqual(bxml.next_borme, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2] + 1))

        url = bxml.get_url_cve("BORME-A-2015-183-04")
        self.assertEqual(url, "https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-04.pdf")

        # from remote file (https)
        bxml = BormeXML.from_file(self.url)
        self.assertEqual(bxml.url, self.url)
        self.assertEqual(bxml.date, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2]))
        self.assertEqual(bxml.filename, None)
        self.assertEqual(bxml.nbo, self.nbo)
        self.assertEqual(bxml.prev_borme, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2] - 1))
        self.assertEqual(bxml.next_borme, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2] + 1))

        # from remote file (insecure http)
        bxml = BormeXML.from_file(self.url, secure=False)
        self.assertEqual(bxml.url, self.url_insecure)
        self.assertEqual(bxml.date, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2]))
        self.assertEqual(bxml.filename, None)
        self.assertEqual(bxml.nbo, self.nbo)
        self.assertEqual(bxml.prev_borme, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2] - 1))
        self.assertEqual(bxml.next_borme, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2] + 1))

        # Exceptions
        self.assertRaises(IOError, BormeXML.from_file, 'invalidfile.xml')

    def test_from_date(self):
        bxml = BormeXML.from_date(self.date)
        self.assertEqual(bxml.url, self.url)
        self.assertEqual(bxml.date, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2]))
        self.assertEqual(bxml.filename, None)
        self.assertEqual(bxml.nbo, self.nbo)
        self.assertEqual(bxml.prev_borme, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2] - 1))
        self.assertEqual(bxml.next_borme, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2] + 1))

        date = datetime.date(*self.date)
        bxml = BormeXML.from_date(date)
        self.assertEqual(bxml.url, self.url)
        self.assertEqual(bxml.date, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2]))
        self.assertEqual(bxml.filename, None)
        self.assertEqual(bxml.nbo, self.nbo)
        self.assertEqual(bxml.prev_borme, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2] - 1))
        self.assertEqual(bxml.next_borme, datetime.date(year=self.date[0], month=self.date[1], day=self.date[2] + 1))

        # Exceptions
        self.assertRaises(BormeDoesntExistException, BormeXML.from_date, (2015, 9, 26))


class BormeXMLTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = os.path.join(EXAMPLES_PATH, 'BORME-S-20150924.xml')
        cls.bxml = BormeXML.from_file(path)

    def test_get_url_pdfs(self):
        urls_a = {'A CORUÑA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-15.pdf',
                  'ALICANTE': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-03.pdf',
                  'ALMERÍA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-04.pdf',
                  'ARABA/ÁLAVA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-01.pdf',
                  'ASTURIAS': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-33.pdf',
                  'BADAJOZ': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-06.pdf',
                  'BARCELONA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-08.pdf',
                  'BURGOS': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-09.pdf',
                  'CANTABRIA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-39.pdf',
                  'CASTELLÓN': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-12.pdf',
                  'CEUTA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-51.pdf',
                  'CUENCA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-16.pdf',
                  'CÁCERES': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-10.pdf',
                  'CÁDIZ': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-11.pdf',
                  'CÓRDOBA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-14.pdf',
                  'HUESCA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-22.pdf',
                  'ILLES BALEARS': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-07.pdf',
                  'LA RIOJA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-26.pdf',
                  'LAS PALMAS': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-35.pdf',
                  'LLEIDA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-25.pdf',
                  'MADRID': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-28.pdf',
                  'MURCIA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-30.pdf',
                  'MÁLAGA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-29.pdf',
                  'NAVARRA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-31.pdf',
                  'OURENSE': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-32.pdf',
                  'PALENCIA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-34.pdf',
                  'PONTEVEDRA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-36.pdf',
                  'SANTA CRUZ DE TENERIFE': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-38.pdf',
                  'SEGOVIA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-40.pdf',
                  'SEVILLA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-41.pdf',
                  'TARRAGONA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-43.pdf',
                  'VALENCIA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-46.pdf',
                  'VALLADOLID': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-47.pdf',
                  'ZAMORA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-49.pdf',
                  'ZARAGOZA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-50.pdf',
                  'ÍNDICE ALFABÉTICO DE SOCIEDADES': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-99.pdf'}

        url_cve_a = {'BORME-A-2015-183-06': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-A-2015-183-06.pdf'}

        urls_b = {'A CORUÑA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-B-2015-183-15.pdf',
                  'ALMERÍA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-B-2015-183-04.pdf',
                  'ILLES BALEARS': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-B-2015-183-07.pdf',
                  'JAÉN': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-B-2015-183-23.pdf',
                  'MADRID': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-B-2015-183-28.pdf',
                  'MÁLAGA': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-B-2015-183-29.pdf'}

        url_cve_b = {'BORME-B-2015-183-04': 'https://www.boe.es/borme/dias/2015/09/24/pdfs/BORME-B-2015-183-04.pdf'}

        urls_c = {'BORME-C-2015-%s.xml' % str(x): 'https://www.boe.es/diario_borme/xml.php?id=BORME-C-2015-%s' % str(x)
            for x in range(9348, 9374 + 1)
            }

        self.assertEqual(self.bxml.get_url_pdfs(seccion=SECCION.A), urls_a)
        self.assertEqual(self.bxml.get_url_pdfs(seccion=SECCION.A, provincia='BADAJOZ'), url_cve_a)
        self.assertEqual(self.bxml.get_url_pdfs(seccion=SECCION.B), urls_b)
        self.assertEqual(self.bxml.get_url_pdfs(seccion=SECCION.B, provincia='ALMERÍA'), url_cve_b)
        self.assertEqual(self.bxml.get_url_pdfs(seccion=SECCION.C), urls_c)
        self.assertRaises(AttributeError, self.bxml.get_url_pdfs)

    def test_get_cves(self):
        seccion_a_bormes = ['BORME-A-2015-183-%s' % x
            for x in ['01', '03', '04', '06', '07', '08', '09', '10', '11', '12', '14', '15', '16',
                      '22', '25', '26', '28', '29', '30', '31', '32', '33', '34', '35', '36', '38',
                      '39', '40', '41', '43', '46', '47', '49', '50', '51']
            ]

        seccion_b_bormes = ['BORME-B-2015-183-%s' % x
            for x in ['04', '07', '15', '23', '28', '29']
            ]

        seccion_c_bormes = ['BORME-C-2015-%s' % str(x)
            for x in range(9348, 9374 + 1)
            ]

        self.assertEqual(self.bxml.get_cves(SECCION.A), seccion_a_bormes)
        self.assertEqual(self.bxml.get_cves(SECCION.A, 'MADRID'), 'BORME-A-2015-183-28')
        self.assertEqual(self.bxml.get_cves(SECCION.B), seccion_b_bormes)
        self.assertEqual(self.bxml.get_cves(SECCION.B, 'MADRID'), 'BORME-B-2015-183-28')
        self.assertEqual(self.bxml.get_cves(SECCION.C), seccion_c_bormes)
        self.assertEqual(self.bxml.get_cves(), seccion_a_bormes + seccion_b_bormes + seccion_c_bormes)

    def test_get_provincias(self):
        provincias = [
            'ARABA/ÁLAVA', 'ALICANTE', 'ALMERÍA', 'BADAJOZ', 'ILLES BALEARS',
            'BARCELONA',  'BURGOS', 'CÁCERES', 'CÁDIZ', 'CASTELLÓN', 'CÓRDOBA',
            'A CORUÑA', 'CUENCA', 'HUESCA', 'LLEIDA', 'LA RIOJA', 'MADRID',
            'MÁLAGA', 'MURCIA', 'NAVARRA', 'OURENSE', 'ASTURIAS', 'PALENCIA',
            'LAS PALMAS', 'PONTEVEDRA', 'SANTA CRUZ DE TENERIFE', 'CANTABRIA',
            'SEGOVIA', 'SEVILLA', 'TARRAGONA', 'VALENCIA', 'VALLADOLID',
            'ZAMORA', 'ZARAGOZA', 'CEUTA']

        self.assertEqual(self.bxml.get_provincias(SECCION.A), provincias)

    def test_get_sizes(self):
        seccion_a_sizes = {'BORME-A-2015-183-01': 264270,
                           'BORME-A-2015-183-03': 245244,
                           'BORME-A-2015-183-04': 169953,
                           'BORME-A-2015-183-06': 161559,
                           'BORME-A-2015-183-07': 267575,
                           'BORME-A-2015-183-08': 370135,
                           'BORME-A-2015-183-09': 157946,
                           'BORME-A-2015-183-10': 161280,
                           'BORME-A-2015-183-11': 164313,
                           'BORME-A-2015-183-12': 160732,
                           'BORME-A-2015-183-14': 152215,
                           'BORME-A-2015-183-15': 227369,
                           'BORME-A-2015-183-16': 171656,
                           'BORME-A-2015-183-22': 161860,
                           'BORME-A-2015-183-25': 161113,
                           'BORME-A-2015-183-26': 161466,
                           'BORME-A-2015-183-28': 517865,
                           'BORME-A-2015-183-29': 244087,
                           'BORME-A-2015-183-30': 173920,
                           'BORME-A-2015-183-31': 179861,
                           'BORME-A-2015-183-32': 157695,
                           'BORME-A-2015-183-33': 159711,
                           'BORME-A-2015-183-34': 154927,
                           'BORME-A-2015-183-35': 162190,
                           'BORME-A-2015-183-36': 163327,
                           'BORME-A-2015-183-38': 230147,
                           'BORME-A-2015-183-39': 175651,
                           'BORME-A-2015-183-40': 150569,
                           'BORME-A-2015-183-41': 282266,
                           'BORME-A-2015-183-43': 175624,
                           'BORME-A-2015-183-46': 212840,
                           'BORME-A-2015-183-47': 153324,
                           'BORME-A-2015-183-49': 153394,
                           'BORME-A-2015-183-50': 186990,
                           'BORME-A-2015-183-51': 160560}

        seccion_b_sizes = {'BORME-B-2015-183-04': 154590,
                           'BORME-B-2015-183-07': 154387,
                           'BORME-B-2015-183-15': 154473,
                           'BORME-B-2015-183-23': 154726,
                           'BORME-B-2015-183-28': 153207,
                           'BORME-B-2015-183-29': 154139}

        seccion_c_sizes = {'BORME-C-2015-9348': 162614,
                           'BORME-C-2015-9349': 154154,
                           'BORME-C-2015-9350': 153806,
                           'BORME-C-2015-9351': 157009,
                           'BORME-C-2015-9352': 154018,
                           'BORME-C-2015-9353': 152244,
                           'BORME-C-2015-9354': 153634,
                           'BORME-C-2015-9355': 153862,
                           'BORME-C-2015-9356': 154451,
                           'BORME-C-2015-9357': 153346,
                           'BORME-C-2015-9358': 155604,
                           'BORME-C-2015-9359': 155331,
                           'BORME-C-2015-9360': 157719,
                           'BORME-C-2015-9361': 155338,
                           'BORME-C-2015-9362': 158391,
                           'BORME-C-2015-9363': 154171,
                           'BORME-C-2015-9364': 157195,
                           'BORME-C-2015-9365': 151230,
                           'BORME-C-2015-9366': 150960,
                           'BORME-C-2015-9367': 152812,
                           'BORME-C-2015-9368': 151345,
                           'BORME-C-2015-9369': 152875,
                           'BORME-C-2015-9370': 154768,
                           'BORME-C-2015-9371': 153658,
                           'BORME-C-2015-9372': 151925,
                           'BORME-C-2015-9373': 157139,
                           'BORME-C-2015-9374': 153469}

        self.assertEqual(self.bxml.get_sizes(SECCION.A), seccion_a_sizes)
        self.assertEqual(self.bxml.get_sizes(SECCION.A, 'MADRID'), {'BORME-A-2015-183-28': 517865})
        self.assertEqual(self.bxml.get_sizes(SECCION.B), seccion_b_sizes)
        self.assertEqual(self.bxml.get_sizes(SECCION.B, 'MADRID'), {'BORME-B-2015-183-28': 153207})
        self.assertEqual(self.bxml.get_sizes(SECCION.C), seccion_c_sizes)

    # get_urls_cve
    # download_borme
    # download_single_borme
    # save_to_file


class BormeCTestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.borme = bormeparser.parse(
                os.path.join(EXAMPLES_PATH, 'BORME-C-2011-20488.xml'),
                SECCION.C)

    def test_instance(self):
        self.assertEqual(self.borme['cifs'], {'A31017494', 'A31067218', 'A58348038', 'B31136005'})
        self.assertEqual(self.borme['cve'], 'BORME-C-2011-20488')
        self.assertEqual(self.borme['departamento'], 'CONVOCATORIAS DE JUNTAS')
        self.assertEqual(self.borme['empresa'], 'DESARROLLOS ESPECIALES DE SISTEMAS DE ANCLAJE, S.A.')
        self.assertEqual(self.borme['fecha'], datetime.date(year=2011, month=5, day=27))
        self.assertEqual(self.borme['seccion'], SECCION.C)
        self.assertEqual(self.borme['diario_numero'], 101)
        self.assertEqual(self.borme['filename'], os.path.join(EXAMPLES_PATH, 'BORME-C-2011-20488.xml'))
        self.assertEqual(self.borme['id_anuncio'], 'A110044738')
        self.assertEqual(self.borme['numero_anuncio'], '44738')
        self.assertEqual(self.borme['pagina_inicial'], 22110)
        self.assertEqual(self.borme['pagina_final'], 22116)
        self.assertEqual(self.borme['seccion'], SECCION.C)


class BormeCTestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.borme = bormeparser.parse(
                os.path.join(EXAMPLES_PATH, 'BORME-C-2011-20488.html'),
                SECCION.C)

    def test_instance(self):
        self.assertEqual(self.borme['cifs'], {'A31017494', 'A31067218', 'A58348038', 'B31136005'})
        self.assertEqual(self.borme['cve'], 'BORME-C-2011-20488')
        self.assertEqual(self.borme['departamento'], 'CONVOCATORIAS DE JUNTAS')
        self.assertEqual(self.borme['diario_numero'], 101)
        self.assertEqual(self.borme['empresa'], 'DESARROLLOS ESPECIALES DE SISTEMAS DE ANCLAJE, S.A.')
        self.assertEqual(self.borme['fecha'], datetime.date(year=2011, month=5, day=27))
        self.assertEqual(self.borme['filename'], os.path.join(EXAMPLES_PATH, 'BORME-C-2011-20488.html'))
        self.assertEqual(self.borme['seccion'], SECCION.C)


if __name__ == '__main__':
    unittest.main()
