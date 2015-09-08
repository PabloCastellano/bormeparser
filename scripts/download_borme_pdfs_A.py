#!/usr/bin/env python
import bormeparser.download
import bormeparser
from bormeparser.exceptions import BormeDoesntExistException
import logging
import os
import sys

# python scripts/download_borme_pdfs_A.py 2015-06-02 [--debug]
if __name__ == '__main__':

    if len(sys.argv) == 3 and sys.argv[2] == '--debug':
        bormeparser.download.logger.setLevel(logging.DEBUG)
    else:
        bormeparser.download.logger.setLevel(logging.INFO)

    try:
        date = tuple(map(int, sys.argv[1].split('-')))
    except:
        print('Invalid date. Use ISO format: 2015-06-02')
        sys.exit(1)
    path = os.path.expanduser('~/.bormes/pdf/%02d/%02d/%02d' % date)
    os.makedirs(path, exist_ok=True)
    seccion = bormeparser.SECCION.A

    print('PATH: %s\nDATE: %s\nSECCION: %s\n' % (path, sys.argv[1], seccion))

    try:
        dl, files = bormeparser.download_pdfs(date, path, seccion=seccion)
        msg = 'SUCCESS' if dl else 'ERROR'
        print('\n%s (%d files downloaded): %s' % (msg, len(files), files))
    except BormeDoesntExistException:
        print('It seems that no BORMEs exist for this date. Nothing was downloaded')
        os.rmdir(path)  # ugly
