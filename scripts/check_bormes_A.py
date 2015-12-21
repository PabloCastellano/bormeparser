#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# check_bormes.py -
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


import bormeparser.download
import bormeparser
from bormeparser.exceptions import BormeDoesntExistException
from bormeparser.borme import BormeXML
from bormeparser.utils import FIRST_BORME

import calendar
import datetime
import logging
import os
import sys

BORMES_ROOT = '~/.bormes'
logger = logging.getLogger('check_bormes')
logger.setLevel(logging.DEBUG)

# python scripts/check_bormes_A.py 2015-06-02 [--debug]


def get_borme_xml_filepath(date):
    year = str(date.year)
    month = '%02d' % date.month
    day = '%02d' % date.day
    filename = 'BORME-S-%d%s%s.xml' % (date.year, month, day)
    return os.path.join(os.path.expanduser(BORMES_ROOT), 'xml', year, month, filename)


def get_borme_pdf_path(date):
    year = str(date.year)
    month = '%02d' % date.month
    day = '%02d' % date.day

    return os.path.join(os.path.expanduser(BORMES_ROOT), 'pdf', year, month, day)


def check_range(begin, end, download_xml=False):
    """ Downloads PDFs using threads """
    next_date = begin
    seccion = bormeparser.SECCION.A
    results = {'good': 0, 'notfound': 0, 'incorrect': 0}

    while next_date and next_date <= end:
        logger.info('Checking %s\n' % next_date.isoformat())
        xml_path = get_borme_xml_filepath(next_date)
        try:
            bxml = BormeXML.from_file(xml_path)
        except FileNotFoundError:
            if download_xml:
                logger.info('Downloading %s' % os.path.basename(xml_path))
                bxml = BormeXML.from_date(next_date)
                os.makedirs(os.path.dirname(xml_path), exist_ok=True)  # TODO: Python 2
                bxml.save_to_file(xml_path)
            else:
                logger.info('XML not found: %s\n' % os.path.basename(xml_path))
                logger.info('If you want to continue specify download_xml=True\n')
                return

        sizes = bxml.get_sizes(seccion)
        path = get_borme_pdf_path(bxml.date)

        for cve, size in sizes.items():
            logger.debug('Checking %s... ' % cve)
            filename = '%s.pdf' % cve
            filepath = os.path.join(path, filename)

            if not os.path.exists(filepath):
                logger.warn('%s: PDF not found\n' % filepath)
                results['notfound'] += 1
                continue

            if os.path.getsize(filepath) != size:
                results['incorrect'] += 1
                logger.warn('%s: PDF size is incorrect (is %d but should be %d)\n' % (filepath, os.path.getsize(filepath), size))
                continue

            results['good'] += 1
            logger.debug('OK\n')

        next_date = bxml.next_borme

    print('\nResults:')
    print('\tGood: %d' % results['good'])
    print('\tIncorrect: %d' % results['incorrect'])
    print('\tNot found: %d' % results['notfound'])


def print_invalid_date():
    print('Invalid date. Use ISO format: 2015-06-02 or 2015-06 or 2015; or --init')
    sys.exit(1)


if __name__ == '__main__':

    ch = logging.StreamHandler()
    ch.terminator = ""

    if len(sys.argv) == 3 and sys.argv[2] == '--debug':
        bormeparser.download.logger.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
        print('DEBUG ON')
    else:
        bormeparser.download.logger.setLevel(logging.INFO)
        ch.setLevel(logging.INFO)
    logger.addHandler(ch)

    if sys.argv[1] == '--init':
        check_range(FIRST_BORME[2009], datetime.date.today())
    else:
        try:
            date = tuple(map(int, sys.argv[1].split('-')))
        except:
            print_invalid_date()

        if len(date) == 3:  # 2015-06-02
            date = datetime.date(*date)
            try:
                check_range(date, date)
            except BormeDoesntExistException:
                print('It looks like there is no BORME for this date. Nothing was downloaded')
        elif len(date) == 2:  # 2015-06
            _, lastday = calendar.monthrange(*date)
            end_date = datetime.date(date[0], date[1], lastday)
            try:
                begin_date = datetime.date(date[0], date[1], 1)
                check_range(begin_date, end_date)
            except BormeDoesntExistException:
                try:
                    begin_date = datetime.date(date[0], date[1], 2)
                    check_range(begin_date, end_date)
                except BormeDoesntExistException:
                    try:
                        begin_date = datetime.date(date[0], date[1], 3)
                        check_range(begin_date, end_date)
                    except BormeDoesntExistException:
                        begin_date = datetime.date(date[0], date[1], 4)
                        check_range(begin_date, end_date)

        elif len(date) == 1:  # 2015
            begin_date = FIRST_BORME[date[0]]
            end_date = datetime.date(date[0], 12, 31)
            check_range(begin_date, end_date)
        else:
            print_invalid_date()
