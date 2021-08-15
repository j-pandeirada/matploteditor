import sys
import numpy as np

from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from plotwindow import PlotWindow
from editorwindow import EditorWindow

class MatPlotEditor():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        
    def plot(self,x,y):
        #initialize the plot window
        self.plot_layout = PlotWindow()

        #initialize the editor window
        self.editor_layout = EditorWindow()

        sc = FigureCanvas(Figure())
        ax = sc.figure.subplots()
        self.editor_layout.bind_axes(ax)

        #-----------------
        line, = self.editor_layout._ax.plot(x,y)
        self.editor_layout.add_line(line)
        self.plot_layout.layout.addWidget(sc)
        self.app.exec_()

if __name__ == "__main__":
    x = np.arange(0,10,0.1)
    y = x**2
    mple = MatPlotEditor()
    mple.plot(x,y)



