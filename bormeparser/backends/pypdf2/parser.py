#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bormeparser.backends.base import BormeParserBackend
from .functions import parse_file


class PyPDF2Parser(BormeParserBackend):
    """
    Parse using PyPDF2
    """
    def _parse(self):
        return parse_file(self.filename)


if __name__ == '__main__':
    import pprint
    actos = parse_file('../../../pdf/BORME-A-2015-27-10.pdf')
    pprint.pprint(actos, width=160)
