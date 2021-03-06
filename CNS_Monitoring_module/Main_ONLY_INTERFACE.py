import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


# GUI FILE
from CNS_Monitoring_module.Interface_ui.ui_mainform import Ui_MainWindow

# IMPORT FUNCTION
from CNS_Monitoring_module.ui_function import *

class Mainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        UIFunction_CLICK.initial_cond(self)
        self.CHART_0 = UIFunction_CHART(parent=self.ui.GP_0_1, title='A1', label=['A', 'B'])
        self.CHART_1 = UIFunction_CHART(parent=self.ui.GP_0_2, title='A2', label=['A', 'B'])

        # >> FUNCTION
        self.ui.Content_menu_empty_0.clicked.connect(lambda: UIFunction_CLICK.toggleMenu(self, 300, True))
        self.ui.Ini_setting.clicked.connect(lambda: UIFunction_CLICK.setInitialCondition(self, True))
        self.ui.Mal_setting.clicked.connect(lambda: UIFunction_CLICK.setMalCondition(self, True))

        # TET
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    sys.exit(app.exec_())