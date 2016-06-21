#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 21 Jun 2016 09:24:48
#
#

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Window import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
