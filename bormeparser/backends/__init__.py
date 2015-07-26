
try:
    from PyPDF2 import PdfFileWriter, PdfFileReader
    import pdfminer
    from .parser1.parser import Parser1
except ImportError:
    pass

from .pypdf2.parser import PyPDF2Parser

__all__ = ['parser1', 'pypdf2']
