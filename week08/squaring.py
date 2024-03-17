# squaring.py
# plot function y = x^2
# author : rahul parvesh dewan

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = "red")
plt.show()

