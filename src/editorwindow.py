from pyparsing import ParseException, ParseFatalException
from PyQt5.QtWidgets import QColorDialog, QMainWindow

from editorwindowui import Ui_MainWindow


class EditorWindow(Ui_MainWindow):
    def __init__(self):
        self._main = QMainWindow()
        self.setupUi(self._main)

        self.titleTextBox.textChanged.connect(self.titleTextBox_handler)
        self.titleFontSizeSpinBox.valueChanged.connect(
            self.titleFontSize_handler
        )
        self.titleFontMenu.activated.connect(self.titleFontMenu_handler)
        self.titleAlignmentMenu.activated.connect(
            self.titleAlignmentMenu_handler
        )
        self.titleFontStyleMenu.activated.connect(
            self.titleFontStyleMenu_handler
        )
        self.titleFontWeightMenu.activated.connect(
            self.titleFontWeightMenu_handler
        )
        self.titleFontColorTextBox.textEdited.connect(
            self.titleFontColorTextBox_handler
        )
        self.titleRotationAngleSpinBox.valueChanged.connect(
            self.titleRotationAngleSpinBox_handler
        )
        self.titleBoxBorderLineStyleMenu.activated.connect(
            self.titleBoxBorderLineStyleMenu_handler
        )
        self.titleBoxBgColorTextBox.textEdited.connect(
            self.titleBoxBgColorTextBox_handler
        )
        self.titleBoxBorderColorTextBox.textEdited.connect(
            self.titleBoxBorderColorTextBox_handler
        )
        self.titleBoxStyleMenu.activated.connect(
            self.titleBoxStyleMenu_handler
        )
        self.titleBoxBorderLineWidthSpinBox.valueChanged.connect(
            self.titleBoxBorderLineWidthSpinBox_handler
        )
        self.titleXOffsetSpinBox.valueChanged.connect(
            self.titleXOffsetSpinBox_handler
        )
        self.titleYOffsetSpinBox.valueChanged.connect(
            self.titleYOffsetSpinBox_handler
        )
        self.titleFontColorPicker.clicked.connect(
            self.titleFontColorPicker_handler
        )
        self.titleBoxBgColorPicker.clicked.connect(
            self.titleBoxBgColorPicker_handler
        )
        self.titleBoxBorderColorPicker.clicked.connect(
            self.titleBoxBorderColorPicker_handler
        )

        self._main.show()

    def bind_axes(self, ax):
        self._ax = ax
        # create an empty title instance with disabled
        # automatic vertical positioning
        self._title = self._ax.set_title("", y=1)
        self._title.set_bbox(dict(facecolor="none", edgecolor="none"))
        self._title_init_pos = self._title.get_position()

    def add_line(self, line):
        self._line = line

    def titleTextBox_handler(self):
        try:
            text = self.titleTextBox.toPlainText()
            # we need to first encode the string to bytes
            text = text.encode("utf-8")
            # and then decode with unicode_escape
            # to properly in order for the linebreaks to work
            text = text.decode("utf-8")
            # decode to utf-8 to have accented chars
            # decode with uniocode_escape to have \n
            self._title.set_text(text)
            self._line.figure.canvas.draw()
        except (ParseException, ParseFatalException):
            pass

    def titleFontColorTextBox_handler(self):
        try:
            color = self.titleFontColorTextBox.text()
            self._title.set_color(color)
        except ValueError:
            color = "black"
            self._title.set_color(color)

        self._line.figure.canvas.draw()

    def titleFontColorPicker_handler(self):
        color = QColorDialog.getColor()
        self.titleFontColorTextBox.setText(color.name())
        self._title.set_color(color.name())
        self._line.figure.canvas.draw()

    def titleXOffsetSpinBox_handler(self):
        xofs = float(self.titleXOffsetSpinBox.value())
        self._title.set_x(self._title_init_pos[0] + xofs / 1000)
        self._line.figure.canvas.draw()

    def titleYOffsetSpinBox_handler(self):
        yofs = float(self.titleYOffsetSpinBox.value())
        self._title.set_y(self._title_init_pos[1] + yofs / 1000)
        self._line.figure.canvas.draw()

    def titleBoxBgColorTextBox_handler(self):
        try:
            color = self.titleBoxBgColorTextBox.text()
            self._title._bbox_patch.update(dict(facecolor=color))
        except ValueError:
            self._title._bbox_patch.update(dict(facecolor="None"))

        self._line.figure.canvas.draw()

    def titleBoxBgColorPicker_handler(self):
        color = QColorDialog.getColor()
        self.titleBoxBgColorTextBox.setText(color.name())
        self._title._bbox_patch.update(dict(facecolor=color.name()))
        self._line.figure.canvas.draw()

    def titleBoxBorderColorTextBox_handler(self):
        try:
            color = self.titleBoxBorderColorTextBox.text()
            self._title._bbox_patch.update(dict(edgecolor=color))
        except ValueError:
            self._title._bbox_patch.update(dict(edgecolor="None"))

        self._line.figure.canvas.draw()

    def titleBoxBorderColorPicker_handler(self):
        color = QColorDialog.getColor()
        self.titleBoxBorderColorTextBox.setText(color.name())
        self._title._bbox_patch.update(dict(edgecolor=color.name()))
        self._line.figure.canvas.draw()

    def titleFontSize_handler(self):
        self._title.set_fontsize(self.titleFontSizeSpinBox.value())
        self._line.figure.canvas.draw()

    def titleFontMenu_handler(self):
        self._title.set_fontfamily(self.titleFontMenu.currentFont().family())
        self._line.figure.canvas.draw()

    def titleAlignmentMenu_handler(self):
        self._title.set_horizontalalignment(
            self.titleAlignmentMenu.currentText()
        )
        self._line.figure.canvas.draw()

    def titleFontStyleMenu_handler(self):
        self._title.set_fontstyle(self.titleFontStyleMenu.currentText())
        self._line.figure.canvas.draw()

    def titleFontWeightMenu_handler(self):
        self._title.set_fontweight(self.titleFontWeightMenu.currentText())
        self._line.figure.canvas.draw()

    def titleRotationAngleSpinBox_handler(self):
        self._title.set_rotation(self.titleRotationAngleSpinBox.value())
        self._line.figure.canvas.draw()

    def titleBoxBorderLineStyleMenu_handler(self):
        linestyle = self.titleBoxBorderLineStyleMenu.currentText()
        self._title._bbox_patch.update(dict(linestyle=linestyle))
        self._line.figure.canvas.draw()

    def titleBoxStyleMenu_handler(self):
        bstyle = self.titleBoxStyleMenu.currentText()
        self._title._bbox_patch.update(dict(boxstyle=bstyle))
        self._line.figure.canvas.draw()

    def titleBoxBorderLineWidthSpinBox_handler(self):
        lwidth = self.titleBoxBorderLineWidthSpinBox.value()
        self._title._bbox_patch.update(dict(linewidth=lwidth))
        self._line.figure.canvas.draw()
