#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BormeException(Exception):
    pass

class BormeIOErrorException(BormeException, IOError):
    pass

class BormeDoesntExistException(BormeException):
    pass

class BormeAlreadyDownloadedException(BormeException):
    pass