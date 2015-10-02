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


# python scripts/download_borme_pdfs_A.py 2015-06-02 [--debug]


# IMPROVEMENT: Threads downloading xml
def download_range(begin, end):
    next_date = begin
    seccion = bormeparser.SECCION.A

    while next_date and next_date <= end:
        bxml = BormeXML.from_date(next_date)
        path = os.path.expanduser('~/.bormes/pdf/%02d/%02d/%02d' % (bxml.date.year, bxml.date.month, bxml.date.day))
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
        download_range(FIRST_BORME, datetime.date.today())
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
            try:
                begin_date = datetime.date(date[0], date[1], 1)
                end_date = datetime.date(date[0], date[1], lastday)
                download_range(begin_date, end_date)
            except BormeDoesntExistException:
                try:
                    begin_date = datetime.date(date[0], date[1], 2)
                    end_date = datetime.date(date[0], date[1], lastday)
                    download_range(begin_date, end_date)
                except BormeDoesntExistException:
                    begin_date = datetime.date(date[0], date[1], 3)
                    end_date = datetime.date(date[0], date[1], lastday)
                    download_range(begin_date, end_date)

        elif len(date) == 1:  # 2015
            try:
                begin_date = datetime.date(date[0], 1, 1)
                end_date = datetime.date(date[0], 12, 31)
                download_range(begin_date, end_date)
            except BormeDoesntExistException:
                try:
                    begin_date = datetime.date(date[0], 1, 2)
                    end_date = datetime.date(date[0], 12, 31)
                    download_range(begin_date, end_date)
                except BormeDoesntExistException:
                    begin_date = datetime.date(date[0], 1, 3)
                    end_date = datetime.date(date[0], 12, 31)
                    download_range(begin_date, end_date)
        else:
            print_invalid_date()
