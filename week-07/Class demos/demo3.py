# ==================================================================================
# Using matplotlib to make visuals
# Sha'Rya Weaver
# 5/20/2026
# ===================================================================================

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# plot is versitile and will take random number of arguments.
plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) # changes the line into a curve.


# For every x,y pair of arguments, there is an optional third argument which is the format string
# The default string is 'b-' which is a solid blue line. 
# The format and strings are from MATLAB.
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis((0, 6, 0, 20)) # takes a list of xmin, xmax, ymin, ymax and specifies the viewport of the Axes
plt.show()


# Illustrates plotting several lines with different format styles in one function call using arrays.
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# 



























































