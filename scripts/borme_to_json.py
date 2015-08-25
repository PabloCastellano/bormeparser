#!/usr/bin/env python
import bormeparser
import bormeparser.borme
import logging
import os
import sys


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: %s <filename.pdf> [--debug]')
        sys.exit(1)

    # set logger DEBUG
    if len(sys.argv) == 3 and sys.argv[2] == '--debug':
        bormeparser.borme.logger.setLevel(logging.DEBUG)

    # filename
    filename = os.path.basename(sys.argv[1]).replace('.pdf', '.json')
    borme = bormeparser.parse(sys.argv[1])
    borme.to_json(filename)

    print()
    print('Created %s' % os.path.abspath(filename))
