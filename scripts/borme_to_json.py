#!/usr/bin/env python
import bormeparser
import bormeparser.borme
import logging
import sys


if __name__ == '__main__':

    # set logger DEBUG
    if len(sys.argv) == 3 and sys.argv[2] == '--debug':
        bormeparser.borme.logger.setLevel(logging.DEBUG)

    # filename
    filename = '%s.json' % sys.argv[1]
    borme = bormeparser.parse(sys.argv[1])
    borme.to_json(filename)

    print()
    print('Created %s' % filename)
