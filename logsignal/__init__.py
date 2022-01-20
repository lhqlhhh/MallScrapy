import logging

from PyQt5.QtCore import QObject
from PyQt5 import QtCore


class Handler(QObject, logging.Handler):
    logSignal = QtCore.pyqtSignal(object)

    def __init__(self):
        super().__init__()
        super(logging.Handler, self).__init__()

    def emit(self, record):
        msg = self.format(record)
        self.logSignal.emit(msg)


class Formatter(logging.Formatter):
    def formatException(self, ei) -> str:
        result = super(Formatter, self).formatException(ei)
        return result

    def format(self, record):
        s = super(Formatter, self).format(record)
        if record.exc_text:
            s = s.replace('\n', '')
        return s

