#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import requests

import bormeparser.backends

# backends
DEFAULT_PARSER = bormeparser.backends.Parser1

# parse: url, filename (string)
def parse(data):

    if os.path.isfile(data):
        # pasar file(data)
        parser = bormeparser.backends.Parser1(data)
        return parser.parse()
    elif data.startswith('http'):
        content = requests.get(data).read()
        parser = bormeparser.backends.Parser1(content)
        return parser.parse()
    else:
        raise ValueError
