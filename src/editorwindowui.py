# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


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
        self.titleFontMenu = QtWidgets.QFontComboBox(self.titleTab)
        self.titleFontMenu.setGeometry(QtCore.QRect(290, 10, 214, 24))
        self.titleFontMenu.setObjectName("titleFontMenu")
        self.titleFontSizeSpinBox = QtWidgets.QSpinBox(self.titleTab)
        self.titleFontSizeSpinBox.setGeometry(QtCore.QRect(570, 10, 46, 26))
        self.titleFontSizeSpinBox.setProperty("value", 12)
        self.titleFontSizeSpinBox.setObjectName("titleFontSizeSpinBox")
        self.titleFontColorTextBox = QtWidgets.QLineEdit(self.titleTab)
        self.titleFontColorTextBox.setGeometry(QtCore.QRect(330, 40, 61, 21))
        self.titleFontColorTextBox.setObjectName("titleFontColorTextBox")
        self.label_2 = QtWidgets.QLabel(self.titleTab)
        self.label_2.setGeometry(QtCore.QRect(290, 40, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.titleTab)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 58, 16))
        self.label_3.setObjectName("label_3")
        self.titleFontStyleMenu = QtWidgets.QComboBox(self.titleTab)
        self.titleFontStyleMenu.setGeometry(QtCore.QRect(50, 90, 76, 24))
        self.titleFontStyleMenu.setObjectName("titleFontStyleMenu")
        self.titleFontStyleMenu.addItem("")
        self.titleFontStyleMenu.addItem("")
        self.titleFontStyleMenu.addItem("")
        self.titleFontWeightMenu = QtWidgets.QComboBox(self.titleTab)
        self.titleFontWeightMenu.setGeometry(QtCore.QRect(190, 90, 76, 24))
        self.titleFontWeightMenu.setObjectName("titleFontWeightMenu")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.titleFontWeightMenu.addItem("")
        self.label_4 = QtWidgets.QLabel(self.titleTab)
        self.label_4.setGeometry(QtCore.QRect(140, 90, 58, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.titleTab)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 121, 16))
        self.label_5.setObjectName("label_5")
        self.titleBoxBgColorTextBox = QtWidgets.QLineEdit(self.titleTab)
        self.titleBoxBgColorTextBox.setGeometry(QtCore.QRect(120, 140, 61, 21))
        self.titleBoxBgColorTextBox.setObjectName("titleBoxBgColorTextBox")
        self.titleAlignmentMenu = QtWidgets.QComboBox(self.titleTab)
        self.titleAlignmentMenu.setGeometry(QtCore.QRect(540, 40, 76, 24))
        self.titleAlignmentMenu.setObjectName("titleAlignmentMenu")
        self.titleAlignmentMenu.addItem("")
        self.titleAlignmentMenu.addItem("")
        self.titleAlignmentMenu.addItem("")
        self.label_6 = QtWidgets.QLabel(self.titleTab)
        self.label_6.setGeometry(QtCore.QRect(470, 40, 71, 16))
        self.label_6.setObjectName("label_6")
        self.titleBoxBorderColorTextBox = QtWidgets.QLineEdit(self.titleTab)
        self.titleBoxBorderColorTextBox.setGeometry(
            QtCore.QRect(340, 140, 61, 21)
        )
        self.titleBoxBorderColorTextBox.setText("")
        self.titleBoxBorderColorTextBox.setObjectName(
            "titleBoxBorderColorTextBox"
        )
        self.label_8 = QtWidgets.QLabel(self.titleTab)
        self.label_8.setGeometry(QtCore.QRect(260, 140, 81, 16))
        self.label_8.setObjectName("label_8")
        self.titleBoxStyleMenu = QtWidgets.QComboBox(self.titleTab)
        self.titleBoxStyleMenu.setGeometry(QtCore.QRect(540, 140, 76, 24))
        self.titleBoxStyleMenu.setObjectName("titleBoxStyleMenu")
        self.titleBoxStyleMenu.addItem("")
        self.titleBoxStyleMenu.addItem("")
        self.titleBoxStyleMenu.addItem("")
        self.label_9 = QtWidgets.QLabel(self.titleTab)
        self.label_9.setGeometry(QtCore.QRect(500, 140, 58, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.titleTab)
        self.label_10.setGeometry(QtCore.QRect(10, 190, 71, 16))
        self.label_10.setObjectName("label_10")
        self.titleBoxBorderLineStyleMenu = QtWidgets.QComboBox(self.titleTab)
        self.titleBoxBorderLineStyleMenu.setGeometry(
            QtCore.QRect(80, 190, 76, 24)
        )
        self.titleBoxBorderLineStyleMenu.setObjectName(
            "titleBoxBorderLineStyleMenu"
        )
        self.titleBoxBorderLineStyleMenu.addItem("")
        self.titleBoxBorderLineStyleMenu.addItem("")
        self.titleBoxBorderLineStyleMenu.addItem("")
        self.titleBoxBorderLineStyleMenu.addItem("")
        self.titleBoxBorderLineStyleMenu.addItem("")
        self.titleBoxBorderLineWidthSpinBox = QtWidgets.QSpinBox(self.titleTab)
        self.titleBoxBorderLineWidthSpinBox.setGeometry(
            QtCore.QRect(240, 190, 46, 26)
        )
        self.titleBoxBorderLineWidthSpinBox.setProperty("value", 5)
        self.titleBoxBorderLineWidthSpinBox.setObjectName(
            "titleBoxBorderLineWidthSpinBox"
        )
        self.label_11 = QtWidgets.QLabel(self.titleTab)
        self.label_11.setGeometry(QtCore.QRect(170, 190, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.titleTab)
        self.label_12.setGeometry(QtCore.QRect(330, 240, 61, 16))
        self.label_12.setObjectName("label_12")
        self.titleRotationAngleSpinBox = QtWidgets.QSpinBox(self.titleTab)
        self.titleRotationAngleSpinBox.setGeometry(
            QtCore.QRect(390, 240, 61, 26)
        )
        self.titleRotationAngleSpinBox.setMaximum(360)
        self.titleRotationAngleSpinBox.setProperty("value", 0)
        self.titleRotationAngleSpinBox.setObjectName(
            "titleRotationAngleSpinBox"
        )
        self.label_14 = QtWidgets.QLabel(self.titleTab)
        self.label_14.setGeometry(QtCore.QRect(10, 240, 51, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.titleTab)
        self.label_15.setGeometry(QtCore.QRect(170, 240, 51, 16))
        self.label_15.setObjectName("label_15")
        self.titleXOffsetSpinBox = QtWidgets.QSpinBox(self.titleTab)
        self.titleXOffsetSpinBox.setGeometry(QtCore.QRect(70, 240, 71, 26))
        self.titleXOffsetSpinBox.setMinimum(-9999)
        self.titleXOffsetSpinBox.setMaximum(9999)
        self.titleXOffsetSpinBox.setStepType(
            QtWidgets.QAbstractSpinBox.DefaultStepType
        )
        self.titleXOffsetSpinBox.setProperty("value", 0)
        self.titleXOffsetSpinBox.setObjectName("titleXOffsetSpinBox")
        self.titleYOffsetSpinBox = QtWidgets.QSpinBox(self.titleTab)
        self.titleYOffsetSpinBox.setGeometry(QtCore.QRect(230, 240, 71, 26))
        self.titleYOffsetSpinBox.setMinimum(-9999)
        self.titleYOffsetSpinBox.setMaximum(9999)
        self.titleYOffsetSpinBox.setStepType(
            QtWidgets.QAbstractSpinBox.DefaultStepType
        )
        self.titleYOffsetSpinBox.setProperty("value", 0)
        self.titleYOffsetSpinBox.setObjectName("titleYOffsetSpinBox")
        self.titleFontColorPicker = QtWidgets.QToolButton(self.titleTab)
        self.titleFontColorPicker.setGeometry(QtCore.QRect(400, 40, 24, 26))
        self.titleFontColorPicker.setObjectName("titleFontColorPicker")
        self.titleBoxBgColorPicker = QtWidgets.QToolButton(self.titleTab)
        self.titleBoxBgColorPicker.setGeometry(QtCore.QRect(190, 140, 24, 26))
        self.titleBoxBgColorPicker.setObjectName("titleBoxBgColorPicker")
        self.titleBoxBorderColorPicker = QtWidgets.QToolButton(self.titleTab)
        self.titleBoxBorderColorPicker.setGeometry(
            QtCore.QRect(410, 140, 24, 26)
        )
        self.titleBoxBorderColorPicker.setObjectName(
            "titleBoxBorderColorPicker"
        )
        self.titleTextBox = QtWidgets.QTextEdit(self.titleTab)
        self.titleTextBox.setGeometry(QtCore.QRect(40, 10, 231, 51))
        self.titleTextBox.setObjectName("titleTextBox")
        self.label_13 = QtWidgets.QLabel(self.titleTab)
        self.label_13.setGeometry(QtCore.QRect(540, 10, 31, 16))
        self.label_13.setObjectName("label_13")
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
        self.tabWidget.setToolTip(
            _translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>"
            )
        )
        self.label.setText(_translate("MainWindow", "Text:"))
        self.label_2.setText(_translate("MainWindow", "Color:"))
        self.label_3.setText(_translate("MainWindow", "Style:"))
        self.titleFontStyleMenu.setItemText(
            0, _translate("MainWindow", "normal")
        )
        self.titleFontStyleMenu.setItemText(
            1, _translate("MainWindow", "italic")
        )
        self.titleFontStyleMenu.setItemText(
            2, _translate("MainWindow", "oblique")
        )
        self.titleFontWeightMenu.setItemText(
            0, _translate("MainWindow", "normal")
        )
        self.titleFontWeightMenu.setItemText(
            1, _translate("MainWindow", "ultralight")
        )
        self.titleFontWeightMenu.setItemText(
            2, _translate("MainWindow", "light")
        )
        self.titleFontWeightMenu.setItemText(
            3, _translate("MainWindow", "regular")
        )
        self.titleFontWeightMenu.setItemText(
            4, _translate("MainWindow", "book")
        )
        self.titleFontWeightMenu.setItemText(
            5, _translate("MainWindow", "medium")
        )
        self.titleFontWeightMenu.setItemText(
            6, _translate("MainWindow", "roman")
        )
        self.titleFontWeightMenu.setItemText(
            7, _translate("MainWindow", "semibold")
        )
        self.titleFontWeightMenu.setItemText(
            8, _translate("MainWindow", "demibold")
        )
        self.titleFontWeightMenu.setItemText(
            9, _translate("MainWindow", "demi")
        )
        self.titleFontWeightMenu.setItemText(
            10, _translate("MainWindow", "bold")
        )
        self.titleFontWeightMenu.setItemText(
            11, _translate("MainWindow", "heavy")
        )
        self.titleFontWeightMenu.setItemText(
            12, _translate("MainWindow", "extra bold")
        )
        self.titleFontWeightMenu.setItemText(
            13, _translate("MainWindow", "black")
        )
        self.label_4.setText(_translate("MainWindow", "Weight:"))
        self.label_5.setText(_translate("MainWindow", "Background Color:"))
        self.titleAlignmentMenu.setItemText(
            0, _translate("MainWindow", "center")
        )
        self.titleAlignmentMenu.setItemText(
            1, _translate("MainWindow", "left")
        )
        self.titleAlignmentMenu.setItemText(
            2, _translate("MainWindow", "right")
        )
        self.label_6.setText(_translate("MainWindow", "Alignment:"))
        self.label_8.setText(_translate("MainWindow", "Border Color:"))
        self.titleBoxStyleMenu.setItemText(
            0, _translate("MainWindow", "square")
        )
        self.titleBoxStyleMenu.setItemText(
            1, _translate("MainWindow", "round")
        )
        self.titleBoxStyleMenu.setItemText(
            2, _translate("MainWindow", "circle")
        )
        self.label_9.setText(_translate("MainWindow", "Style:"))
        self.label_10.setText(_translate("MainWindow", "Line Style:"))
        self.titleBoxBorderLineStyleMenu.setItemText(
            0, _translate("MainWindow", "solid")
        )
        self.titleBoxBorderLineStyleMenu.setItemText(
            1, _translate("MainWindow", "dashed")
        )
        self.titleBoxBorderLineStyleMenu.setItemText(
            2, _translate("MainWindow", "dashdot")
        )
        self.titleBoxBorderLineStyleMenu.setItemText(
            3, _translate("MainWindow", "dotted")
        )
        self.titleBoxBorderLineStyleMenu.setItemText(
            4, _translate("MainWindow", "none")
        )
        self.label_11.setText(_translate("MainWindow", "Line Width:"))
        self.label_12.setText(_translate("MainWindow", "Rotation:"))
        self.label_14.setText(_translate("MainWindow", "X offset:"))
        self.label_15.setText(_translate("MainWindow", "Y offset:"))
        self.titleFontColorPicker.setText(_translate("MainWindow", "..."))
        self.titleBoxBgColorPicker.setText(_translate("MainWindow", "..."))
        self.titleBoxBorderColorPicker.setText(_translate("MainWindow", "..."))
        self.label_13.setText(_translate("MainWindow", "Size:"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.titleTab),
            _translate("MainWindow", "Title"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.axisTab),
            _translate("MainWindow", "Axis"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.dataTab),
            _translate("MainWindow", "Data"),
        )
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
