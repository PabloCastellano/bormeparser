from .acto import ACTO
from .borme import Borme, BormeXML
from .cargo import CARGO
from .config import CONFIG
from .download import download_xml, download_pdfs, download_pdf
from .download import get_url_pdf, get_url_pdfs, get_url_xml
from .emisor import EMISOR
from .parser import parse
from .provincia import PROVINCIA
from .seccion import SECCION

"""
FIXME:

import logging
logger = logging.getLogger(__name__)
# To change the logging level of bormeparser use this code in your program:
#  import bormeparser
#  import logging
#  bormeparser.logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)
ch = logging.StreamHandler()
logger.addHandler(ch)
"""
