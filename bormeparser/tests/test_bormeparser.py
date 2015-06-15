#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_bormeparser.py -
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
import os
import six
import tempfile
import unittest

import bormeparser
from bormeparser.borme import Borme
from bormeparser.exceptions import BormeDoesntExistException

DATA = {(2015, 6, 2):
            {'xml': 'http://www.boe.es/diario_borme/xml.php?id=BORME-S-20150602',
             'pdf': {(bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA):
                         'http://boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-29.pdf',
                     bormeparser.SECCION.A:
                         {'ZARAGOZA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-50.pdf',
                                     'BURGOS': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-09.pdf',
                                     'GRANADA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-18.pdf',
                                     u'\xcdNDICE ALFAB\xc9TICO DE SOCIEDADES': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-99.pdf',
                                     'MADRID': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-28.pdf',
                                     'ILLES BALEARS': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-07.pdf',
                                     'CIUDAD REAL': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-13.pdf',
                                     'GIRONA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-17.pdf',
                                     'TARRAGONA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-43.pdf',
                                     'VALLADOLID': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-47.pdf',
                                     u'LE\xd3N': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-24.pdf',
                                     'PONTEVEDRA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-36.pdf',
                                     'ALICANTE': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-03.pdf',
                                     u'JA\xc9N': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-23.pdf',
                                     'VALENCIA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-46.pdf',
                                     'LLEIDA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-25.pdf',
                                     'LAS PALMAS': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-35.pdf',
                                     'ALBACETE': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-02.pdf',
                                     'BADAJOZ': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-06.pdf',
                                     'BARCELONA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-08.pdf',
                                     'LA RIOJA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-26.pdf',
                                     u'M\xc1LAGA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-29.pdf',
                                     'PALENCIA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-34.pdf',
                                     u'ALMER\xcdA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-04.pdf',
                                     'MURCIA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-30.pdf',
                                     u'A CORU\xd1A': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-15.pdf',
                                     'TOLEDO': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-45.pdf',
                                     'BIZKAIA': 'http://www.boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-48.pdf'
                         }
                    }
            }
       }


class BormeparserUrlsTestCase(unittest.TestCase):
    date = (2015, 6, 2)

    def test_url_xml_tuple(self):
        url = bormeparser.get_url_xml(self.date)
        self.assertEqual(url, DATA[self.date]['xml'])

    def test_url_xml_date(self):
        date = datetime.date(*self.date)
        url = bormeparser.get_url_xml(date)
        self.assertEqual(url, DATA[self.date]['xml'])

    def test_url_pdf_tuple(self):
        url = bormeparser.get_url_pdf(self.date, bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA)
        self.assertEqual(url, DATA[self.date]['pdf'][(bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA)])

    def test_url_pdf_date(self):
        date = datetime.date(*self.date)
        url = bormeparser.get_url_pdf(date, bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA)
        self.assertEqual(url, DATA[self.date]['pdf'][(bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA)])

    def test_url_pdfs_tuple(self):
        urls = bormeparser.get_url_pdfs(self.date, bormeparser.SECCION.A)
        six.assertCountEqual(self, urls, DATA[self.date]['pdf'][bormeparser.SECCION.A])

    def test_url_pdfs_date(self):
        date = datetime.date(*self.date)
        urls = bormeparser.get_url_pdfs(date, bormeparser.SECCION.A)
        six.assertCountEqual(self, urls, DATA[self.date]['pdf'][bormeparser.SECCION.A])


class BormeparserInvalidDateTestCase(unittest.TestCase):
    date = (2015, 6, 31)

    def test_url_xml(self):
        self.assertRaises(ValueError, bormeparser.get_url_xml, self.date)

    def test_url_pdf(self):
        self.assertRaises(ValueError, bormeparser.get_url_pdf, self.date, bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA)

    def test_url_pdfs(self):
        self.assertRaises(ValueError, bormeparser.get_url_pdfs, self.date, bormeparser.SECCION.A)


class BormeparserBormeDoesntExistTestCase(unittest.TestCase):
    date = (2015, 6, 6)

    def test_url_pdf(self):
        self.assertRaises(BormeDoesntExistException, bormeparser.get_url_pdf, self.date, bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA)

    def test_url_pdfs(self):
        self.assertRaises(BormeDoesntExistException, bormeparser.get_url_pdfs, self.date, bormeparser.SECCION.A)


class BormeparserDownloadTestCase(unittest.TestCase):
    date = (2015, 6, 2)

    def test_download_xml(self):
        path = os.path.join(tempfile.gettempdir(), '20150602.xml')
        downloaded = bormeparser.download_xml(self.date, path)
        self.assertTrue(downloaded)
        self.assertEqual(os.path.getsize(path), 31590)
        os.unlink(path)

    # TODO: Get size from xml: urlPdf/szBytes
    def test_download_pdf(self):
        path = os.path.join(tempfile.gettempdir(), 'BORME-A-2015-102-29.pdf')
        borme = bormeparser.download_pdf(self.date, path, bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA)
        self.assertIsInstance(borme, Borme)
        self.assertEqual(os.path.getsize(path), 202795)
        os.unlink(path)

    def test_download_pdf(self):
        # Maybe these are too many files to download
        pass


class BormeparserParserTestCase(unittest.TestCase):
    date = (2015, 6, 2)

    def test_parser(self):
        path = os.path.join(tempfile.gettempdir(), 'BORME-A-2015-102-29.pdf')
        # data = parse(path)
        pass

if __name__ == '__main__':
    unittest.main()
