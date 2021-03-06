#!/usr/bin/env python

"""
This module implements exceptions raised in Content Ingestion Server.
"""

class NotImplementedException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class FileAlreadyExistsException(Exception):
    pass

class TranscodingException(Exception):
    pass

class ThumbExtractionException(Exception):
    pass

class AVInfoException(Exception):
    pass

class FileTransferException(Exception):
    pass
