#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# download_borme_pdfs_C.py - Download BORME C PDF files
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


import bormeparser
from bormeparser.exceptions import BormeDoesntExistException
from bormeparser.borme import BormeXML
from bormeparser.utils import FIRST_BORME
from common import *

import argparse
import datetime
import logging
import os

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
logger.addHandler(ch)


def download_range(begin, end, directory):
    """ Downloads PDFs C using threads """
    next_date = begin
    seccion = bormeparser.SECCION.C
    total_downloaded = 0

    while next_date and next_date <= end:
        path = get_borme_pdf_path(next_date, directory)
        xml_path = get_borme_xml_filepath(next_date, directory)
        logger.info('\nDownloading files from {} (sección {}) to {}\n'.format(next_date, seccion, path))
        try:
            bxml = BormeXML.from_file(xml_path)
            if bxml.next_borme:
                logger.debug('{filename} already exists!'.format(filename=os.path.basename(xml_path)))
            else:
                logger.debug('Re-downloading {filename}'.format(filename=os.path.basename(xml_path)))
                bxml = BormeXML.from_date(next_date)
                try:
                    os.makedirs(os.path.dirname(xml_path))
                except OSError:
                    pass
                bxml.save_to_file(xml_path)

        except FileNotFoundError:
            logger.debug('Downloading {filename}'.format(filename=os.path.basename(xml_path)))
            bxml = BormeXML.from_date(next_date)
            try:
                os.makedirs(os.path.dirname(xml_path))
            except OSError:
                pass
            bxml.save_to_file(xml_path)

        try:
            os.makedirs(path)
            _, files = bxml.download_borme(path, seccion=seccion)
            total_downloaded += len(files)
        except OSError:
            # Si existe el directorio, pasar al siguiente día
            print('Skipping dir')

        next_date = bxml.next_borme

    logger.info('\n{} files were downloaded'.format(total_downloaded))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download BORME A PDF files.')
    parser.add_argument('-f', '--fromdate', required=True, help='ISO formatted date (ex. 2015-01-01) or "init"')
    parser.add_argument('-t', '--to', required=True, help='ISO formatted date (ex. 2016-01-01) or "today"')
    parser.add_argument('-d', '--directory', default=DEFAULT_BORME_ROOT, help='Directory to download files (default is {})'.format(DEFAULT_BORME_ROOT))
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Verbose mode')
    args = parser.parse_args()

    bormeparser.borme.logger.setLevel(logging.ERROR)
    if args.verbose:
        bormeparser.download.logger.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)
    else:
        bormeparser.download.logger.setLevel(logging.ERROR)
        logger.setLevel(logging.INFO)

    if args.fromdate == 'init':
        date_from = FIRST_BORME[2009]
    else:
        date_from = datetime.datetime.strptime(args.fromdate, '%Y-%m-%d').date()

    if args.to == 'today':
        date_to = datetime.date.today()
    else:
        date_to = datetime.datetime.strptime(args.to, '%Y-%m-%d').date()

    try:
        download_range(date_from, date_to, args.directory)
    except BormeDoesntExistException:
        logger.warn('It looks like there is no BORME for the start date ({}). Nothing was downloaded'.format(date_from))
