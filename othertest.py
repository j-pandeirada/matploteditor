import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
y = x**2
#mple = MatPlotEditor()
plt.figure()
plt.plot(x,y)
plt.plot(x,y**2)
plt.show()