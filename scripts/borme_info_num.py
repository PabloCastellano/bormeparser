#!/usr/bin/env python
import bormeparser
import bormeparser.borme
import bormeparser.backends.pypdf2.functions
from bormeparser.exceptions import BormeAnuncioNotFound
import logging
import sys


# TODO: Fusionar con borme_info.py
# file.pdf 233232 [--debug]
# file.pdf 223234,223243,223244,223250,223253,223254 [--debug]
if __name__ == '__main__':

    # set logger DEBUG
    if len(sys.argv) == 4 and sys.argv[3] == '--debug':
        bormeparser.borme.logger.setLevel(logging.DEBUG)
        bormeparser.backends.pypdf2.functions.logger.setLevel(logging.DEBUG)  # FIXME: DEFAULT_PARSER

    borme = bormeparser.parse(sys.argv[1])

    for id in sys.argv[2].split(','):
        try:
            anuncio = borme.get_anuncio(int(id))
            print('Anuncio %d' % anuncio.id)
            print('-' * (8 + len(str(anuncio.id))))
            print()
            for acto, valor in anuncio.get_actos():
                print('  %s' % acto)
                print('    %s' % valor)
            print('  Datos registrales')
            print('    %s' % anuncio.datos_registrales)
        except BormeAnuncioNotFound:
            print('No existe el anuncio %s' % id)
        print()
