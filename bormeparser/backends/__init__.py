
try:
    from PyPDF2 import PdfFileWriter, PdfFileReader
    import pdfminer
    from .parser1.parser import Parser1
except ImportError:
    pass

from .defaults import OPTIONS
from .pypdf2.parser import PyPDF2Parser
from .seccion_c.lxml.parser import LxmlBormeCParser

__all__ = ['parser1', 'pypdf2', 'seccion_c']
