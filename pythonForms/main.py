import sys
from PyQt4.QtGui import QMainWindow, QApplication
import myFirstForm

#Initialise window
class MyWindow(QMainWindow, myFirstForm.Ui_frmMain):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        #Events here
        self.cmdQuit.clicked.connect(self.closeApplication)
        self.menuQuit.triggered.connect(self.closeApplication)

    #Event handlers here
    def closeApplication(self):
        self.close()


myApplication = QApplication(sys.argv)
applicationWin = MyWindow()
applicationWin.show()
sys.exit(myApplication.exec_())
