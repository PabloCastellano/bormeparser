#!/usr/bin/env python
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

# python scripts/download_borme_pdfs_A.py 2015-06-02 [--debug]


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


def download_range(begin, end):
    """ Downloads PDFs using threads """
    next_date = begin
    seccion = bormeparser.SECCION.A

    #end = min(end, datetime.date.today())
    while next_date and next_date <= end:
        print('####### %s ' % next_date)
        xml_path = get_borme_xml_filepath(next_date)
        try:
            bxml = BormeXML.from_file(xml_path)
            if bxml.next_borme:
                print('%s already exists!' % os.path.basename(xml_path))
            else:
                print('Re-downloading %s ' % os.path.basename(xml_path))
                bxml = BormeXML.from_date(next_date)
                os.makedirs(os.path.dirname(xml_path), exist_ok=True)  # TODO: Python 2
                bxml.save_to_file(xml_path)

        except FileNotFoundError:
            print('Downloading %s ' % os.path.basename(xml_path))
            bxml = BormeXML.from_date(next_date)
            os.makedirs(os.path.dirname(xml_path), exist_ok=True)  # TODO: Python 2
            bxml.save_to_file(xml_path)

        path = get_borme_pdf_path(bxml.date)
        os.makedirs(path, exist_ok=True)

        print('\nPATH: %s\nDATE: %s\nSECCION: %s\n' % (path, bxml.date, seccion))
        bxml.download_pdfs(path, seccion=seccion)
        next_date = bxml.next_borme


def print_invalid_date():
    print('Invalid date. Use ISO format: 2015-06-02 or 2015-06 or 2015; or --init')
    sys.exit(1)


if __name__ == '__main__':

    if len(sys.argv) == 3 and sys.argv[2] == '--debug':
        bormeparser.download.logger.setLevel(logging.DEBUG)
    else:
        bormeparser.download.logger.setLevel(logging.INFO)

    if sys.argv[1] == '--init':
        download_range(FIRST_BORME[2009], datetime.date.today())
    else:
        try:
            date = tuple(map(int, sys.argv[1].split('-')))
        except:
            print_invalid_date()

        if len(date) == 3:  # 2015-06-02
            date = datetime.date(*date)
            try:
                download_range(date, date)
            except BormeDoesntExistException:
                print('It looks like there is no BORME for this date. Nothing was downloaded')
        elif len(date) == 2:  # 2015-06
            _, lastday = calendar.monthrange(*date)
            end_date = datetime.date(date[0], date[1], lastday)
            try:
                begin_date = datetime.date(date[0], date[1], 1)
                download_range(begin_date, end_date)
            except BormeDoesntExistException:
                try:
                    begin_date = datetime.date(date[0], date[1], 2)
                    download_range(begin_date, end_date)
                except BormeDoesntExistException:
                    try:
                        begin_date = datetime.date(date[0], date[1], 3)
                        download_range(begin_date, end_date)
                    except BormeDoesntExistException:
                        begin_date = datetime.date(date[0], date[1], 4)
                        download_range(begin_date, end_date)

        elif len(date) == 1:  # 2015
            begin_date = FIRST_BORME[date[0]]
            end_date = datetime.date(date[0], 12, 31)
            download_range(begin_date, end_date)
        else:
            print_invalid_date()
