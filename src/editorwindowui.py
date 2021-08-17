# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 451))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.titleTab = QtWidgets.QWidget()
        self.titleTab.setAutoFillBackground(True)
        self.titleTab.setObjectName("titleTab")
        self.label = QtWidgets.QLabel(self.titleTab)
        self.label.setGeometry(QtCore.QRect(10, 10, 58, 16))
        self.label.setObjectName("label")
        self.titleTextBox = QtWidgets.QLineEdit(self.titleTab)
        self.titleTextBox.setGeometry(QtCore.QRect(50, 10, 311, 21))
        self.titleTextBox.setObjectName("titleTextBox")
        self.titleFontMenu = QtWidgets.QFontComboBox(self.titleTab)
        self.titleFontMenu.setGeometry(QtCore.QRect(10, 40, 214, 24))
        self.titleFontMenu.setObjectName("titleFontMenu")
        self.titleFontSize = QtWidgets.QSpinBox(self.titleTab)
        self.titleFontSize.setGeometry(QtCore.QRect(230, 40, 46, 26))
        self.titleFontSize.setProperty("value", 12)
        self.titleFontSize.setObjectName("titleFontSize")
        self.colorTextBox = QtWidgets.QLineEdit(self.titleTab)
        self.colorTextBox.setGeometry(QtCore.QRect(330, 40, 61, 21))
        self.colorTextBox.setObjectName("colorTextBox")
        self.label_2 = QtWidgets.QLabel(self.titleTab)
        self.label_2.setGeometry(QtCore.QRect(290, 40, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.titleTab)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 58, 16))
        self.label_3.setObjectName("label_3")
        self.fontStyleMenu = QtWidgets.QComboBox(self.titleTab)
        self.fontStyleMenu.setGeometry(QtCore.QRect(50, 80, 76, 24))
        self.fontStyleMenu.setObjectName("fontStyleMenu")
        self.fontStyleMenu.addItem("")
        self.fontStyleMenu.addItem("")
        self.fontStyleMenu.addItem("")
        self.fontWeightMenu = QtWidgets.QComboBox(self.titleTab)
        self.fontWeightMenu.setGeometry(QtCore.QRect(190, 80, 76, 24))
        self.fontWeightMenu.setObjectName("fontWeightMenu")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.fontWeightMenu.addItem("")
        self.label_4 = QtWidgets.QLabel(self.titleTab)
        self.label_4.setGeometry(QtCore.QRect(140, 80, 58, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.titleTab)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 121, 16))
        self.label_5.setObjectName("label_5")
        self.bgColorTextBox = QtWidgets.QLineEdit(self.titleTab)
        self.bgColorTextBox.setGeometry(QtCore.QRect(120, 120, 61, 21))
        self.bgColorTextBox.setObjectName("bgColorTextBox")
        self.alignmentMenu = QtWidgets.QComboBox(self.titleTab)
        self.alignmentMenu.setGeometry(QtCore.QRect(470, 40, 76, 24))
        self.alignmentMenu.setObjectName("alignmentMenu")
        self.alignmentMenu.addItem("")
        self.alignmentMenu.addItem("")
        self.alignmentMenu.addItem("")
        self.label_6 = QtWidgets.QLabel(self.titleTab)
        self.label_6.setGeometry(QtCore.QRect(400, 40, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.titleTab)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 121, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.borderColorTextBox = QtWidgets.QLineEdit(self.titleTab)
        self.borderColorTextBox.setGeometry(QtCore.QRect(270, 120, 61, 21))
        self.borderColorTextBox.setText("")
        self.borderColorTextBox.setObjectName("borderColorTextBox")
        self.label_8 = QtWidgets.QLabel(self.titleTab)
        self.label_8.setGeometry(QtCore.QRect(190, 120, 81, 16))
        self.label_8.setObjectName("label_8")
        self.boxStyleMenu = QtWidgets.QComboBox(self.titleTab)
        self.boxStyleMenu.setGeometry(QtCore.QRect(390, 120, 76, 24))
        self.boxStyleMenu.setObjectName("boxStyleMenu")
        self.boxStyleMenu.addItem("")
        self.boxStyleMenu.addItem("")
        self.boxStyleMenu.addItem("")
        self.label_9 = QtWidgets.QLabel(self.titleTab)
        self.label_9.setGeometry(QtCore.QRect(350, 120, 58, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.titleTab)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_10.setObjectName("label_10")
        self.borderlineStyle = QtWidgets.QComboBox(self.titleTab)
        self.borderlineStyle.setGeometry(QtCore.QRect(80, 160, 76, 24))
        self.borderlineStyle.setObjectName("borderlineStyle")
        self.borderlineStyle.addItem("")
        self.borderlineStyle.addItem("")
        self.borderlineStyle.addItem("")
        self.borderlineStyle.addItem("")
        self.borderlineStyle.addItem("")
        self.borderLineWidth = QtWidgets.QSpinBox(self.titleTab)
        self.borderLineWidth.setGeometry(QtCore.QRect(240, 160, 46, 26))
        self.borderLineWidth.setProperty("value", 5)
        self.borderLineWidth.setObjectName("borderLineWidth")
        self.label_11 = QtWidgets.QLabel(self.titleTab)
        self.label_11.setGeometry(QtCore.QRect(170, 160, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.titleTab)
        self.label_12.setGeometry(QtCore.QRect(390, 80, 71, 16))
        self.label_12.setObjectName("label_12")
        self.rotationAngle = QtWidgets.QSpinBox(self.titleTab)
        self.rotationAngle.setGeometry(QtCore.QRect(450, 80, 61, 26))
        self.rotationAngle.setMaximum(360)
        self.rotationAngle.setProperty("value", 0)
        self.rotationAngle.setObjectName("rotationAngle")
        self.label_14 = QtWidgets.QLabel(self.titleTab)
        self.label_14.setGeometry(QtCore.QRect(370, 10, 51, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.titleTab)
        self.label_15.setGeometry(QtCore.QRect(510, 10, 51, 16))
        self.label_15.setObjectName("label_15")
        self.xOffset = QtWidgets.QSpinBox(self.titleTab)
        self.xOffset.setGeometry(QtCore.QRect(430, 10, 71, 26))
        self.xOffset.setMinimum(-9999)
        self.xOffset.setMaximum(9999)
        self.xOffset.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.xOffset.setProperty("value", 0)
        self.xOffset.setObjectName("xOffset")
        self.yOffset = QtWidgets.QSpinBox(self.titleTab)
        self.yOffset.setGeometry(QtCore.QRect(560, 10, 71, 26))
        self.yOffset.setMinimum(-9999)
        self.yOffset.setMaximum(9999)
        self.yOffset.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.yOffset.setProperty("value", 0)
        self.yOffset.setObjectName("yOffset")
        self.tabWidget.addTab(self.titleTab, "")
        self.axisTab = QtWidgets.QWidget()
        self.axisTab.setObjectName("axisTab")
        self.tabWidget.addTab(self.axisTab, "")
        self.dataTab = QtWidgets.QWidget()
        self.dataTab.setObjectName("dataTab")
        self.tabWidget.addTab(self.dataTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Figure Editor"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Text:"))
        self.label_2.setText(_translate("MainWindow", "Color:"))
        self.label_3.setText(_translate("MainWindow", "Style:"))
        self.fontStyleMenu.setItemText(0, _translate("MainWindow", "normal"))
        self.fontStyleMenu.setItemText(1, _translate("MainWindow", "italic"))
        self.fontStyleMenu.setItemText(2, _translate("MainWindow", "oblique"))
        self.fontWeightMenu.setItemText(0, _translate("MainWindow", "normal"))
        self.fontWeightMenu.setItemText(1, _translate("MainWindow", "ultralight"))
        self.fontWeightMenu.setItemText(2, _translate("MainWindow", "light"))
        self.fontWeightMenu.setItemText(3, _translate("MainWindow", "regular"))
        self.fontWeightMenu.setItemText(4, _translate("MainWindow", "book"))
        self.fontWeightMenu.setItemText(5, _translate("MainWindow", "medium"))
        self.fontWeightMenu.setItemText(6, _translate("MainWindow", "roman"))
        self.fontWeightMenu.setItemText(7, _translate("MainWindow", "semibold"))
        self.fontWeightMenu.setItemText(8, _translate("MainWindow", "demibold"))
        self.fontWeightMenu.setItemText(9, _translate("MainWindow", "demi"))
        self.fontWeightMenu.setItemText(10, _translate("MainWindow", "bold"))
        self.fontWeightMenu.setItemText(11, _translate("MainWindow", "heavy"))
        self.fontWeightMenu.setItemText(12, _translate("MainWindow", "extra bold"))
        self.fontWeightMenu.setItemText(13, _translate("MainWindow", "black"))
        self.label_4.setText(_translate("MainWindow", "Weight:"))
        self.label_5.setText(_translate("MainWindow", "Background Color:"))
        self.alignmentMenu.setItemText(0, _translate("MainWindow", "center"))
        self.alignmentMenu.setItemText(1, _translate("MainWindow", "left"))
        self.alignmentMenu.setItemText(2, _translate("MainWindow", "right"))
        self.label_6.setText(_translate("MainWindow", "Alignment:"))
        self.label_8.setText(_translate("MainWindow", "Border Color:"))
        self.boxStyleMenu.setItemText(0, _translate("MainWindow", "square"))
        self.boxStyleMenu.setItemText(1, _translate("MainWindow", "round"))
        self.boxStyleMenu.setItemText(2, _translate("MainWindow", "circle"))
        self.label_9.setText(_translate("MainWindow", "Style:"))
        self.label_10.setText(_translate("MainWindow", "Line Style:"))
        self.borderlineStyle.setItemText(0, _translate("MainWindow", "solid"))
        self.borderlineStyle.setItemText(1, _translate("MainWindow", "dashed"))
        self.borderlineStyle.setItemText(2, _translate("MainWindow", "dashdot"))
        self.borderlineStyle.setItemText(3, _translate("MainWindow", "dotted"))
        self.borderlineStyle.setItemText(4, _translate("MainWindow", "none"))
        self.label_11.setText(_translate("MainWindow", "Line Width:"))
        self.label_12.setText(_translate("MainWindow", "Rotation:"))
        self.label_14.setText(_translate("MainWindow", "X offset:"))
        self.label_15.setText(_translate("MainWindow", "Y offset:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.titleTab), _translate("MainWindow", "Title"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.axisTab), _translate("MainWindow", "Axis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dataTab), _translate("MainWindow", "Data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save As..."))
        self.actionLoad.setText(_translate("MainWindow", "Open..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
