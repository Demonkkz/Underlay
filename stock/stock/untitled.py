# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_finance import candlestick_ochl


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=6, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.axes = fig.add_subplot(111)
        self.axes.xaxis_date()
        self.axes.autoscale_view()
        fig.autofmt_xdate(bottom=0.2, rotation=40, ha='right', which=None)

    def plot(self, tuples):
        candlestick_ochl(self.axes, tuples, width=0.6, colorup='r', colordown="g", alpha=0.8)


class Ui_widget(object):
    def setupUi(self, widget: object):
        widget.setObjectName("widget")
        widget.setEnabled(True)
        widget.resize(800, 400)
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(widget)
        self.openGLWidget_2.setGeometry(QtCore.QRect(270, 80, 251, 171))
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.graphicview = QtWidgets.QGraphicsView(widget)
        self.graphicview.setGeometry(QtCore.QRect(20, 80, 251, 171))
        self.graphicview.setObjectName("graphicview")
        self.btn_1 = QtWidgets.QPushButton(widget)
        self.btn_1.setGeometry(QtCore.QRect(320, 20, 75, 23))
        self.btn_1.setObjectName("btn_1")
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 72, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(widget)
        self.label_3.setGeometry(QtCore.QRect(270, 60, 54, 12))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(widget)
        self.comboBox.setGeometry(QtCore.QRect(228, 20, 74, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btn_2 = QtWidgets.QPushButton(widget)
        self.btn_2.setGeometry(QtCore.QRect(400, 20, 75, 23))
        self.btn_2.setObjectName("btn_2")
        self.lineEdit = QtWidgets.QLineEdit(widget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 123, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "股票预测分析"))
        self.btn_1.setText(_translate("widget", "OK"))
        self.label.setText(_translate("widget", "输入股票代码"))
        self.label_2.setText(_translate("widget", "历史曲线"))
        self.label_3.setText(_translate("widget", "预测曲线"))
        self.comboBox.setItemText(0, _translate("widget", " "))
        self.comboBox.setItemText(1, _translate("widget", "最近30天"))
        self.comboBox.setItemText(2, _translate("widget", "最近60天"))
        self.btn_2.setText(_translate("widget", "Cancel"))

    def plot(self, tuples):
        dr = Figure_Canvas()
        dr.plot(tuples)  # 画图
        self.graphicscene = QtWidgets.QGraphicsScene()
        self.graphicscene.addWidget(dr)
        self.graphicview.setScene(self.graphicscene)
        self.graphicview.show()
