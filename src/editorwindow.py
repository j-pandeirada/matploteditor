from PyQt5.QtWidgets import QMainWindow, QColorDialog
from PyQt5.QtGui import QIcon
from editorwindowui import Ui_MainWindow


class EditorWindow(Ui_MainWindow):
    def __init__(self):
        # super().__init__()
        # self._main = QtWidgets.QWidget()
        self._main = QMainWindow()
        self.setupUi(self._main)
        
        self.titleTextBox.textChanged.connect(self.titleTextBox_handler)
        self.titleFontSize.valueChanged.connect(self.titleFontSize_handler)
        self.titleFontMenu.activated.connect(self.titleFontMenu_handler)
        self.alignmentMenu.activated.connect(self.alignmentMenu_handler)
        self.fontStyleMenu.activated.connect(self.fontStyleMenu_handler)
        self.fontWeightMenu.activated.connect(self.fontWeightMenu_handler)
        self.colorTextBox.textEdited.connect(self.colorTextBox_handler)
        self.rotationAngle.valueChanged.connect(self.rotationAngle_handler)
        self.borderlineStyle.activated.connect(self.borderlineStyle_handler)
        self.bgColorTextBox.textEdited.connect(self.bgColorTextBox_handler)
        self.borderColorTextBox.textEdited.connect(
            self.borderColorTextBox_handler
        )
        self.boxStyleMenu.activated.connect(self.boxStyleMenu_handler)
        self.borderLineWidth.valueChanged.connect(self.borderLineWidth_handler)
        self.xOffset.valueChanged.connect(self.xOffset_handler)
        self.yOffset.valueChanged.connect(self.yOffset_handler)
        self.titleColorPicker.clicked.connect(self.titleColorPicker_handler)
        self.bgColorPicker.clicked.connect(self.bgColorPicker_handler)
        self.borderColorPicker.clicked.connect(self.borderColorPicker_handler)

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
        try:
            text = self.titleTextBox.toPlainText()
            # we need to first encode the string to bytes
            text = text.encode('utf-8')
            # and then decode with unicode_escape
            # to properly in order for the linebreaks to work
            text = text.decode('utf-8')
            # decode to utf-8 to have accented chars
            # decode with uniocode_escape to have \n
            self._title.set_text(text)
            self._line.figure.canvas.draw()
        except:
            pass

    def colorTextBox_handler(self):
        try:
            color= self.colorTextBox.text()
            self._title.set_color(color)
        except:
            color = 'black'
            self._title.set_color(color)
        
        self._line.figure.canvas.draw()
    
    def titleColorPicker_handler(self):
        color = QColorDialog.getColor()
        self.colorTextBox.setText(color.name())
        self._title.set_color(color.name())
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
        try:
            color = self.bgColorTextBox.text()
            self._title._bbox_patch.update(dict(facecolor=color))
        except:
            self._title._bbox_patch.update(dict(facecolor='None'))
        
        self._line.figure.canvas.draw()
    
    def bgColorPicker_handler(self):
        color = QColorDialog.getColor()
        self.bgColorTextBox.setText(color.name())
        self._title._bbox_patch.update(dict(facecolor=color.name()))
        self._line.figure.canvas.draw()

    def borderColorTextBox_handler(self):
        try:
            color = self.borderColorTextBox.text()
            self._title._bbox_patch.update(dict(edgecolor=color))
        except:
            self._title._bbox_patch.update(dict(edgecolor='None'))

        self._line.figure.canvas.draw()

    def borderColorPicker_handler(self):
        color = QColorDialog.getColor()
        self.borderColorTextBox.setText(color.name())
        self._title._bbox_patch.update(dict(edgecolor=color.name()))
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
