from PyQt5 import QtWidgets

from editorwindowui import Ui_MainWindow


class EditorWindow(Ui_MainWindow):
    def __init__(self):
        # super().__init__()
        # self._main = QtWidgets.QWidget()
        self._main = QtWidgets.QMainWindow()
        self.setupUi(self._main)
        self.titleTextBox.returnPressed.connect(self.titleTextBox_handler)
        self.titleFontSize.valueChanged.connect(self.titleFontSize_handler)
        self.titleFontMenu.activated.connect(self.titleFontMenu_handler)
        self.alignmentMenu.activated.connect(self.alignmentMenu_handler)
        self.fontStyleMenu.activated.connect(self.fontStyleMenu_handler)
        self.fontWeightMenu.activated.connect(self.fontWeightMenu_handler)
        self.colorTextBox.returnPressed.connect(self.colorTextBox_handler)
        self.rotationAngle.valueChanged.connect(self.rotationAngle_handler)
        self.borderlineStyle.activated.connect(self.borderlineStyle_handler)
        self.bgColorTextBox.returnPressed.connect(self.bgColorTextBox_handler)
        self.borderColorTextBox.returnPressed.connect(
            self.borderColorTextBox_handler
        )
        self.boxStyleMenu.activated.connect(self.boxStyleMenu_handler)
        self.borderLineWidth.valueChanged.connect(self.borderLineWidth_handler)
        self.xOffset.valueChanged.connect(self.xOffset_handler)
        self.yOffset.valueChanged.connect(self.yOffset_handler)

        self._main.show()

    def bind_axes(self, ax):
        self._ax = ax
        #create an empty title instance with disabled
        #automatic vertical positioning
        self._title = self._ax.set_title("",y=1)
        self._title.set_bbox(dict(facecolor="none", edgecolor="none"))
        self._title_init_pos = self._title.get_position()

    def add_line(self, line):
        self._line = line

    def titleTextBox_handler(self):
        text = self.titleTextBox.text()
        # we need to first encode the string to bytes
        text = text.encode('utf-8')
        # and then decode with unicode_escape
        # to properly in order for the linebreaks to work
        text = text.decode('unicode_escape')
        self._title.set_text(text)
        self._line.figure.canvas.draw()

    def colorTextBox_handler(self):
        self._title.set_color(self.colorTextBox.text())
        self._line.figure.canvas.draw()
    
    def xOffset_handler(self):
        xofs = float(self.xOffset.value())
        self._title.set_x(self._title_init_pos[0]+xofs/1000)
        self._line.figure.canvas.draw()
    
    def yOffset_handler(self):
        yofs = float(self.yOffset.value())
        self._title.set_y(self._title_init_pos[1]+yofs/1000)
        self._line.figure.canvas.draw()

    def bgColorTextBox_handler(self):
        color = self.bgColorTextBox.text()
        self._title._bbox_patch.update(dict(facecolor=color))
        self._line.figure.canvas.draw()

    def borderColorTextBox_handler(self):
        color = self.borderColorTextBox.text()
        self._title._bbox_patch.update(dict(edgecolor=color))
        self._line.figure.canvas.draw()

    def titleFontSize_handler(self):
        self._title.set_fontsize(self.titleFontSize.value())
        self._line.figure.canvas.draw()

    def titleFontMenu_handler(self):
        self._title.set_fontfamily(self.titleFontMenu.currentFont().family())
        self._line.figure.canvas.draw()

    def alignmentMenu_handler(self):
        self._title.set_horizontalalignment(self.alignmentMenu.currentText())
        self._line.figure.canvas.draw()

    def fontStyleMenu_handler(self):
        self._title.set_fontstyle(self.fontStyleMenu.currentText())
        self._line.figure.canvas.draw()

    def fontWeightMenu_handler(self):
        self._title.set_fontweight(self.fontWeightMenu.currentText())
        self._line.figure.canvas.draw()

    def rotationAngle_handler(self):
        self._title.set_rotation(self.rotationAngle.value())
        self._line.figure.canvas.draw()

    def borderlineStyle_handler(self):
        linestyle = self.borderlineStyle.currentText()
        self._title._bbox_patch.update(dict(linestyle=linestyle))
        self._line.figure.canvas.draw()

    def boxStyleMenu_handler(self):
        bstyle = self.boxStyleMenu.currentText()
        self._title._bbox_patch.update(dict(boxstyle=bstyle))
        self._line.figure.canvas.draw()

    def borderLineWidth_handler(self):
        lwidth = self.borderLineWidth.value()
        self._title._bbox_patch.update(dict(linewidth=lwidth))
        self._line.figure.canvas.draw()
