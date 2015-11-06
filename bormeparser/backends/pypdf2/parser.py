#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from __future__ import absolute_import
#from functions import parse_file
from .functions import parse_file, logger
from bormeparser.backends.base import BormeParserBackend
import logging


class PyPDF2Parser(BormeParserBackend):
    """
    Parse using PyPDF2
    """
    def __init__(self, filename, log_level=logging.WARN):
        super(PyPDF2Parser, self).__init__(filename)
        logger.setLevel(log_level)

    def _parse(self):
        return parse_file(self.filename)


if __name__ == '__main__':
    import pprint
    actos = parse_file('../../../pdf/BORME-A-2015-27-10.pdf')
    pprint.pprint(actos, width=160)
