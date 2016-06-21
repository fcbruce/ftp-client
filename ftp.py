#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Mon 20 Jun 2016 21:10:36
#
#

import os
from ftplib import FTP
from PyQt5.QtNetwork import *
from PyQt5.QtGui import *

def create_ftp(address, username, password):

    try:
        ftp = FTP(address)
        result = ftp.login(username, password)
        return ftp

    except:

        return None

def ftp_upload(ftp, fname, progress):

    ftp_upload.do_size = 0
    ftp_upload.total_size = os.stat(fname).st_size
    # ftp_upload.th = th
    ftp_upload.prog = progress

    print 'total size' , ftp_upload.total_size

    def update(x):

        ftp_upload.do_size += 1024
        print ftp_upload.do_size
        # ftp_upload.th.emit(SIGNAL('PROGRESS'), ftp_upload.do_size/ftp_upload.total_size * 100.0)
        # ftp_upload.th.update.emit(ftp_upload.do_size/ftp_upload.total_size * 100.0)
        ftp_upload.prog.setValue(ftp_upload.do_size/ftp_upload.total_size * 100.0)
    
    try:
        file = open(fname, 'rb')
        print 'open!'
        ftp.storbinary('STOR ' + os.path.basename(fname), file, 1024, update)
        return True
    except:
        return False

def ftp_download(ftp, fname, progress):

    print fname

    ftp_download.do_size = 0;
    ftp_download.total_size = ftp.size(fname)
    ftp_download.prog = progress

    def update():

        ftp_download.do_size += 1024
        print ftp_download.do_size
        ftp_download.prog.setValue(ftp_download.do_size/ftp_download.total_size * 100.0)

    try:
        ftp_download.file = open(fname, 'wb')

        def cb(x):
            ftp_download.file.write(x)
            update()

        ftp.retrbinary('RETR ' + fname, cb, 1024)
        ftp_download.file.close()
        return True
    except:
        ftp_download.file.close()
        return False



if __name__ == '__main__':

    ftp = create_ftp('128.199.118.35', 'ftpuser1', 'greedisgood')

    if ftp:
        print ftp

        ftp_upload(ftp, '/home/fcbruce/ftp-py/main.py')
    else:
        print 'null'

    # ftp = FTP('128.199.118.35')
    # result =  ftp.login('ftpuser1', 'greedisgood')
    # print result

    # print ftp.pwd()


    # # ftp.storlines('STOR text.txt', open('test.txt', 'r'))
    # ftp.retrlines('LIST')

    # file = open('text.txt', 'wb')
    # ftp.retrbinary('RETR text.txt', file.write)
    # file.close()
