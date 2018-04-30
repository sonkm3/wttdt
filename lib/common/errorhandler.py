# -*- coding: utf-8 -*-
import sys
import traceback


class ErrorHandler(object):
    @staticmethod
    def handle():
        sys.stderr.write("\n")
        sys.stderr.write("----------------------------\n")
        sys.stderr.write(sys.exc_info()[1].__class__.__name__ + "\n")
        sys.stderr.write("----------------------------\n")
        sys.stderr.write(str(sys.exc_info()[1].__dict__) + "\n")
        sys.stderr.write("----------------------------\n")
        sys.stderr.write(traceback.format_exc())
        sys.stderr.write("\n")
        sys.stderr.write("----------------------------\n")
