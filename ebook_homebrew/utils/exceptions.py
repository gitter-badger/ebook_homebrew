# -*- coding: utf-8 -*-
"""Exception Classes
"""


class BaseError(Exception):
    pass


class ChangeFileNameError(BaseError):
    def __init__(self, error_class, message):
        self.error_class = error_class
        self.message = message

    def __str__(self):
        return "{error_class}: {message}".format(error_class=self.error_class, message=self.message)


class MakePDFError(BaseError):
    def __init__(self, error_class, message):
        self.error_class = error_class
        self.message = message

    def __str__(self):
        return "{error_class}: {message}".format(error_class=self.error_class, message=self.message)


class MakeZIPError(BaseError):
    def __init__(self, error_class, message):
        self.error_class = error_class
        self.message = message

    def __str__(self):
        return "{error_class}: {message}".format(error_class=self.error_class, message=self.message)


class ZipFileExistError(MakeZIPError):
    def __init__(self):
        self.error_class = "ZipFileExistError"
        self.message = "Already Zipfile you decide name exist." \
                       "If overwrite, choose 'overwrite' parameter."


class InvalidDigitsFormat(ChangeFileNameError):
    def __init__(self):
        self.error_class = "ChangeFileNameError"
        self.message = "Invalid serial number digit value. " \
                       "If you want to use multiple digits, " \
                       "please divide into comma separator"


class InvalidNumberParameterType(ChangeFileNameError):
    def __init__(self):
        self.error_class = "InvalidNumberParameterType"
        self.message = "To create new file name, must be used 'Integer'."


class InvalidImageParameterType(ChangeFileNameError):
    def __init__(self):
        self.error_class = "InvalidImageParameterType"
        self.message = "To check image file, must be 'Image file' such as jpeg, png, or gif."


class InvalidImageFileFormat(MakePDFError):
    def __init__(self):
        self.error_class = "InvalidImageFileFormat"
        self.message = "Not supported file format. Supported 'jpg', 'png', 'gif'"


class ChangeFileNameOSError(ChangeFileNameError):
    def __init__(self):
        self.error_class = "ChangeFileNameOSError"
        self.message = "OSError was occurred. Reading more message above."
