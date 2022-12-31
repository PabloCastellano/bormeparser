#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# borme_poller.py -
# Copyright (C) 2015 Pablo Castellano <pablo@anche.no>
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


# El BORME se publica los días laborables y normalmente a las 7:30 de la mañana
import datetime
import requests
import time

URL_BASE = 'https://boe.es/diario_borme/xml.php?id=BORME-S-'  # https://boe.es/diario_borme/xml.php?id=BORME-S-20150910
DELAY = 5 * 60  # 5 minutes
LOGFILE = 'xmlpoller.log'
TIMEOUT = 10


def parse_content(content):
    """
    '<?xml version="1.0"?>\n<error><descripcion>No se encontr&#xF3; el sumario original.</descripcion></error>\n'
    """

    # Python 3
    found = False
    if isinstance(content, bytes):
        content = content.decode('unicode_escape')

    fp = open(LOGFILE, 'a')
    fp.write(str(datetime.datetime.now()) + '\n')
    print(datetime.datetime.now())
    if '<error>' in content:
        fp.write('Not available yet. I will try again in %d minutes.' % (DELAY / 60))
        print('Not available yet. I will try again in %d minutes.' % (DELAY / 60))
    else:
        fp.write('AVAILABLE! (%d bytes)' % len(content))
        print('AVAILABLE! (%d bytes)' % len(content))
        found = True

    fp.write('\n\n')
    fp.close()
    return found


def wait_till_seven():
    now = datetime.datetime.now()
    fp = open(LOGFILE, 'a')
    fp.write(str(now) + '\n')
    print(now)
    fp.write('Sleep until next 7:00')
    print('Sleep until next 7:00')
    fp.write('\n\n')
    fp.close()
    wake_date = datetime.datetime.now() + datetime.timedelta(days=1)
    wake_date = wake_date.replace(hour=7, minute=0, second=0, microsecond=0)
    wake_seconds = (wake_date - datetime.datetime.now()).total_seconds()
    time.sleep(wake_seconds)


def wait_till_monday(weekday):
    now = datetime.datetime.now()
    fp = open(LOGFILE, 'a')
    fp.write(str(now) + '\n')
    print(now)
    fp.write('Sleep until next Monday 7:00')
    print('Sleep until next Monday 7:00')
    fp.write('\n\n')
    fp.close()

    n = (0 - now.weekday()) % 7  # Days till next Monday
    wake_date = now + datetime.timedelta(days=n)
    wake_date = wake_date.replace(hour=7, minute=0, second=0, microsecond=0)
    wake_seconds = (wake_date - datetime.datetime.now()).total_seconds()
    time.sleep(wake_seconds)


def poll_xml_dl():
    while True:
        today = datetime.date.today()
        weekday = today.weekday()
        if weekday in (5, 6):
            wait_till_monday(weekday)
        url = URL_BASE + today.strftime('%Y%m%d')
        req = requests.get(url, timeout=TIMEOUT)
        found = parse_content(req.text)
        if found:
            wait_till_seven()
        else:
            time.sleep(DELAY)


if __name__ == '__main__':
    poll_xml_dl()
