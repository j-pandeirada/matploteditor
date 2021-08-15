import numpy as np

from src.matploteditor import MatPlotEditor

if __name__ == "__main__":
    x = np.arange(0, 10, 0.1)
    y = x ** 2
    mple = MatPlotEditor()
    mple.plot(x, y)
