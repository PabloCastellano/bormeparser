#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# borme_json_date.py - Convert BORME PDF files to JSON for a specific date range
# Copyright (C) 2015-2022 Pablo Castellano <pablo@anche.no>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import bormeparser
import bormeparser.borme

from bormeparser.backends.defaults import OPTIONS
from bormeparser.utils import FIRST_BORME
OPTIONS['SANITIZE_COMPANY_NAME'] = True

import argparse
import datetime
import os
import time

from threading import Thread
from queue import Queue

BORME_ROOT = bormeparser.CONFIG["borme_root"]
THREADS = 6


class ThreadConvertJSON(Thread):
    def __init__(self, queue):
        super(ThreadConvertJSON, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            pdf_path, json_path = self.queue.get()
            print('Creating %s ...' % json_path)
            try:
                borme = bormeparser.parse(pdf_path, bormeparser.SECCION.A)
                borme.to_json(json_path)
                print('{cve}: OK'.format(cve=borme.cve))
            except Exception as e:
                print('ERROR: {} ({})'.format(os.path.basename(pdf_path), e))
            self.queue.task_done()


def walk_borme_root_date(bormes_root, date):
    pdf_root = os.path.join(bormes_root, 'pdf')
    year, month, day = str(date.year), '{:02d}'.format(date.month), '{:02d}'.format(date.day)
    pdf_day_dir = os.path.join(pdf_root, year, month, day)
    if not os.path.isdir(pdf_day_dir):
        print("No existe {}".format(pdf_day_dir))
        return None, None, None

    _, _, files = next(os.walk(pdf_day_dir))
    for filename in files:
        yield pdf_day_dir, filename


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert all BORME PDF files to JSON.')
    parser.add_argument('-d', '--directory', default=BORME_ROOT, help='Directory to download files (default is {})'.format(BORME_ROOT))
    parser.add_argument('-f', '--fromdate', default='today', help='ISO formatted date (ex. 2015-01-01) or "init". Default: today')
    parser.add_argument('-t', '--to', default='today', help='ISO formatted date (ex. 2016-01-01). Default: today')

    args = parser.parse_args()

    if args.fromdate == 'init':
        date_from = FIRST_BORME[2009]
    elif args.fromdate == 'today':
        date_from = datetime.date.today()
    else:
        date_from = datetime.datetime.strptime(args.fromdate, '%Y-%m-%d').date()

    if args.to == 'today':
        date_to = datetime.date.today()
    else:
        date_to = datetime.datetime.strptime(args.to, '%Y-%m-%d').date()

    start_time = time.time()

    q = Queue()
    for i in range(THREADS):
        t = ThreadConvertJSON(q)
        t.setDaemon(True)
        t.start()

    date = date_from
    while date <= date_to:
        for day_dir, filename in walk_borme_root_date(args.directory, date):
            if filename and not filename.endswith('.pdf') or filename.endswith('-99.pdf'):
                continue
            year, month, day = str(date.year), '{:02d}'.format(date.month), '{:02d}'.format(date.day)
            json_day_dir = os.path.join(args.directory, "json", year, month, day)
            os.makedirs(json_day_dir, exist_ok=True)

            pdf_path = os.path.join(day_dir, filename)
            json_filename = filename.replace('.pdf', '.json')
            json_path = os.path.join(json_day_dir, json_filename)
            q.put((pdf_path, json_path))
        date += datetime.timedelta(days=1)
    q.join()

    elapsed_time = time.time() - start_time
    print('Elapsed time: %.2f seconds' % elapsed_time)
