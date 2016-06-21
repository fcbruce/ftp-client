#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 21 Jun 2016 20:42:04
#
#

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
from ftp import *

class upload_thread(QThread):

    update = pyqtSignal()
    
    def __init__(self, parent, ftp, log, fname):

        super(upload_thread, self).__init__(parent)
        self.ftp = ftp
        self.log = log
        self.fname = fname
        print 'init!'

    def run(self):

        print 'upload'

        if self.fname[0]: 
            
            self.log.append('upload ' + self.fname[0])
            if ftp_upload(self, self.ftp, self.fname[0]):
                self.log.append('upload success')
            else:
                self.log.append('upload failed')

        print 'run'


