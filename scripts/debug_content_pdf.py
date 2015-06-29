#!/usr/bin/env python
import sys
from PyPDF2 import PdfFileReader


if __name__ == '__main__':
    reader = PdfFileReader(open(sys.argv[1], 'rb'))
    for n in range(0, reader.getNumPages()):
        content = reader.getPage(n).getContents().getData()

        # Python 3
        if isinstance(content, bytes):
            content = content.decode('unicode_escape')

        #print(content)
        for line in content.split('\n'):
            print(line)
