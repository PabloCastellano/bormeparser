#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class BormeParserBackend(object):
    def __init__(self, filename):

        if not os.path.isfile(filename):
            raise IOError

        self.filename = filename

    def parse(self):
        raise NotImplementedError

    def parse_actos(self):
        raise NotImplementedError
