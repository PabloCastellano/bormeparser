#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from bormeparser.borme import Borme, BormeActo
from bormeparser.regex import regex_fecha


class BormeParserBackend(object):
    def __init__(self, filename):

        if not os.path.isfile(filename):
            raise IOError

        self.filename = filename

    def parse(self):
        actos = self._parse()
        bormeactos = []
        for id_acto in actos.keys():
            if not isinstance(id_acto, int):
                continue
            data = actos[id_acto]
            a = BormeActo(id_acto, data['Empresa'], data['Actos'])
            bormeactos.append(a)

        fecha = regex_fecha(actos['borme_fecha'])
        # FIXME: provincia, seccion objects
        return Borme(fecha, actos['borme_seccion'], actos['borme_provincia'], actos['borme_num'], bormeactos)

    def _parse(self):
        """
        :return: diccionario con key= id del acto y value {'Empresa': str, 'Actos': dict}
        """
        raise NotImplementedError

    def parse_actos(self):
        self._parse_actos()

    def _parse_actos(self):
        raise NotImplementedError
