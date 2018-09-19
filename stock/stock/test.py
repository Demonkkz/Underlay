from untitled import Ui_widget  # 导入uitestPyQt5.ui转换为uitestPyQt5.py中的类

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import sys
from plotKline import plot_K_line


class Mywindow(QtWidgets.QWidget, Ui_widget):

    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.btn_1.clicked.connect(self.on_click)
        self.btn_2.clicked.connect(self.ch_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        value1 = self.lineEdit.text()
        value2 = self.comboBox.currentText()
        tuples = plot_K_line(value1, int(value2[2:4]))
        Ui_widget.plot(self, tuples)

    def ch_click(self):
        self.lineEdit.setText('')
        self.comboBox.setCurrentIndex(0)


app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())
