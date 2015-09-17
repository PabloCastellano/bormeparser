#!/usr/bin/env python
import bormeparser.download
import bormeparser
from bormeparser.exceptions import BormeDoesntExistException
import calendar
import logging
import os
import sys

# python scripts/download_borme_pdfs_A.py 2015-06-02 [--debug]

def download(date):
    path = os.path.expanduser('~/.bormes/pdf/%02d/%02d/%02d' % date)
    os.makedirs(path, exist_ok=True)
    seccion = bormeparser.SECCION.A

    print('PATH: %s\nDATE: %s\nSECCION: %s\n' % (path, date, seccion))

    try:
        dl, files = bormeparser.download_pdfs(date, path, seccion=seccion)
        msg = 'SUCCESS' if dl else 'ERROR'
        print('\n%s (%d files downloaded): %s' % (msg, len(files), files))
    except BormeDoesntExistException:
        print('It seems that no BORMEs exist for this date. Nothing was downloaded')
        os.rmdir(path)  # ugly


def invalid_date():
    print('Invalid date. Use ISO format: 2015-06-02 or 2015-06 or 2015')
    sys.exit(1)


if __name__ == '__main__':

    if len(sys.argv) == 3 and sys.argv[2] == '--debug':
        bormeparser.download.logger.setLevel(logging.DEBUG)
    else:
        bormeparser.download.logger.setLevel(logging.INFO)

    try:
        date = tuple(map(int, sys.argv[1].split('-')))
    except:
        invalid_date()

    if len(date) == 3:  # 2015
        download(date)
    elif len(date) == 2:  # 2015-06
        _, lastday = calendar.monthrange(*date)
        for day in range(1, lastday+1):
            fulldate = date + (day,)
            download(fulldate)
    elif len(date) == 1:  # 2015-06-02
        for month in range(1, 13):
            _, lastday = calendar.monthrange(date[0], month)
            for day in range(1, lastday+1):
                fulldate = date + (month, day)
                download(fulldate)
    else:
        invalid_date()

