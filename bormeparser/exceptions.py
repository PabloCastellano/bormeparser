#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BormeparserException(Exception):
    pass


class BormeIOErrorException(BormeparserException, IOError):
    pass


class BormeDoesntExistException(BormeparserException):
    pass


class BormeAlreadyDownloadedException(BormeparserException):
    pass


class BormeInvalidActoException(BormeparserException):
    pass


class BormeAnuncioNotFound(BormeparserException):
    pass
