# -*- coding: utf-8 -*-
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 21 Jun 2016 09:21:41
#
#

import sys
import threading
import thread
from threads import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ftp import *

class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.resize(800, 600)

        self.L_address = QLabel('Server Address', self)
        self.L_address.resize(100, 30)
        self.L_address.move(20, 20)

        self.address = QLineEdit(self)
        self.address.resize(100, 30)
        self.address.move(20, 50)

        self.L_username = QLabel('Username', self)
        self.L_username.resize(100, 30)
        self.L_username.move(20, 80)

        self.username = QLineEdit(self)
        self.username.resize(100, 30)
        self.username.move(20, 110)

        self.L_password = QLabel('Password', self)
        self.L_password.resize(100, 30)
        self.L_password.move(20, 140)

        self.password = QLineEdit(self)
        self.password.resize(100, 30)
        self.password.move(20, 170)
        self.password.setEchoMode(2)

        self.B_connect = QPushButton('Connect', self)
        self.B_connect.resize(100, 30)
        self.B_connect.move(20, 210)
        self.B_connect.clicked.connect(self.do_check_connect)

        self.log = QTextEdit(self)
        self.log.resize(100, 300)
        self.log.move(20, 250)
        self.log.setReadOnly(True)

        self.B_upload = QPushButton(self)
        self.B_upload.setText('Upload')
        self.B_upload.resize(120, 40)
        self.B_upload.move(660, 520)
        self.B_upload.clicked.connect(self.do_upload)
        self.B_upload.setEnabled(False)

        self.B_download = QPushButton(self)
        self.B_download.setText('Download')
        self.B_download.resize(120, 40)
        self.B_download.move(660, 460)
        self.B_download.clicked.connect(self.do_download)
        self.B_download.setEnabled(False)

        self.filelist = QListWidget(self)
        self.filelist.resize(630, 400)
        self.filelist.move(150, 20)

        self.progress = QProgressBar(self)
        self.progress.resize(440, 60)
        self.progress.move(150, 480)

    def do_check_connect(self):

        # t = threading.Thread(target=self.check_connect)
        # t.start()
        self.check_connect()

    def check_connect(self):

        self.log.append('connecting to server')

        ftp = create_ftp(self.address.text(), self.username.text(), self.password.text())

        if ftp: 

            self.log.append('connect success')
            self.ftp = ftp
            self.refresh()
            self.B_upload.setEnabled(True)
            self.B_download.setEnabled(True)
        else:

            self.log.append('connect failed')

    def refresh(self):

        self.filelist.clear()
        files = []
        #self.ftp.dir(files.append)
        files = self.ftp.nlst()
        print files
        for line in files:
            self.filelist.addItem(line)
            print line

    def do_upload(self):

        self.upload()

        #print 'upload'
        #fname = QFileDialog.getOpenFileName(self, 'Choose file')
        #self.t = upload_thread(self, self.ftp, self.log, fname)
        ## t = thread.start_new_thread(self.upload, (fname))
        #self.t.update.connect(self.update_progress)
        #self.t.start()
        ## self.connect(t, SIGNAL('PROGRESS'), self.update_progress)

    def upload(self):

        fname = QFileDialog.getOpenFileName(self, 'Choose file')

        if fname[0]: 
            
            self.log.append('upload ' + fname[0])
            if ftp_upload(self.ftp, fname[0], self.progress):
                self.log.append('upload success')
                self.refresh()
            else:
                self.log.append('upload failed')

    def do_download(self):

        # thread.start_new_thread(self.download, ())
        # t.start()
        self.download()

    def download(self):

        item = self.filelist.currentItem()

        if item:
            fname = str(item.text())
            self.log.append('download ' + fname)
            print 'fname = ' + fname
            if (ftp_download(self.ftp, fname, self.progress)):
                self.log.append('download success')
            else:
                self.log.append('download failed')

    def update_progress(self, val):

        self.progress.setValue(val)

