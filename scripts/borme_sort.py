#!/usr/bin/env python
import bormeparser
import bormeparser.borme
import bormeparser.backends.pypdf2.functions
import logging
import os
import sys


# python scripts/borme_sort.py /home/libreborme/.bormes/pdf/2015/06/01
if __name__ == '__main__':

    # set logger DEBUG
    if len(sys.argv) == 3 and sys.argv[2] == '--debug':
        bormeparser.borme.logger.setLevel(logging.DEBUG)
        bormeparser.backends.pypdf2.functions.logger.setLevel(logging.DEBUG)  # FIXME: DEFAULT_PARSER

    bormes = []
    _, _, files = next(os.walk(sys.argv[1]))
    for f in files:
        # TODO: Solo seccion.A
        if f.endswith('-99.pdf'):
            continue
        path = os.path.join(sys.argv[1], f)
        bormes.append(bormeparser.parse(path))

    for borme in sorted(bormes):
        print(borme.filename)
        print('  CVE: %s' % borme.cve)
        print('  Rango de anuncios: %d-%d' % (borme.anuncios_rango[0], borme.anuncios_rango[1]))
        print()
