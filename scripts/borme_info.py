#!/usr/bin/env python
import bormeparser
import sys


if __name__ == '__main__':
    borme = bormeparser.parse(sys.argv[1])
    print('CVE: %s' % borme.cve)
    print('Fecha: %s' % borme.date)
    print('Num: %s' % borme.num)
    print('Provincia: %s' % borme.provincia)
    print('Seccion: %s' % borme.seccion)
    print('Actos incluidos: %d' % len(borme.get_actos()))
