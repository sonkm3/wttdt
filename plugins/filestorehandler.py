# -*- coding: utf-8 -*-
import datetime, json, os
from lib.common.statushandlerabstract import StatusHandlerAbstract

class FilestoreHandler(StatusHandlerAbstract):

    def __init__(self, directory, prefix='', rotatecount=1000):
        self.directory = directory
        self.prefix = prefix
        self.fileobj = self.get_fileobj(self.get_filepath(self.directory, self.prefix))
        self.rotatecount = rotatecount
        self.count = 0

    def get_fileobj(self, path):
        return open(path, mode='wt')

    def get_filepath(self, directory, prefix):
        dt = datetime.datetime.now()
        filename = str(prefix) + '%04d%02d%02d-%02d%02d%02d.txt' % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        return os.path.realpath(os.path.expanduser(os.path.normpath(directory))) + '/' + filename

    def rotate_fileobj(self):
        self.fileobj.flush()
        self.fileobj.close()
        self.fileobj = self.get_fileobj(self.get_filepath(self.directory, self.prefix))
        self.count=0

    def handle(self, each_response):
        if each_response.decode('utf-8').strip() == "":
            pass
        else:
            each_line = each_response.decode('utf-8').strip()
            if(each_line.isprintable() and not each_line.isspace()):

                if self.count>=self.rotatecount:
                    self.rotate_fileobj()

                self.fileobj.write(each_line)
                self.fileobj.write("\n")
                self.count += 1
        return

    def destruct(self):
        self.fileobj.close()
        # sys.stderr.write('destruct:' + self.__class__.__name__ + "\n")
