import sys

import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtWidgets

from editorwindow import EditorWindow
from plotwindow import PlotWindow


class MatPlotEditor:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

    def plot(self, x, y):
        # initialize the plot window
        self.plot_layout = PlotWindow()

        # initialize the editor window
        self.editor_layout = EditorWindow()

        sc = FigureCanvasQTAgg(Figure())
        ax = sc.figure.subplots()
        self.editor_layout.bind_axes(ax)

        # -----------------
        (line,) = self.editor_layout._ax.plot(x, y)
        self.editor_layout.add_line(line)
        self.plot_layout.layout.addWidget(sc)
        self.app.exec_()


if __name__ == "__main__":
    x_data = np.arange(0, 10, 0.1)
    y_data = x_data ** 2
    mple = MatPlotEditor()
    mple.plot(x_data, y_data)
