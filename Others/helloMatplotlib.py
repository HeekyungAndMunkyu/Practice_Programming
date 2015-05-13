import numpy as np
import matplotlib

# this line prepare IPython for working with matplotlib
%matplotlib inline

# this actually impors matplotlib
import matplotlib.pyplot as plt

x = np.linespace(0, 10, 30) #array of 30 points from 0 to 10
y = np.sin(x)
z = y + np.random.normal(size=30) * .2
plt.plot(x, y, 'ro-', label='A sine wave')
plt.plot(x, z, 'b-', label='Noisy sine')
plt.legend(loc = 'lower right')
plt.xlable("X axis")
plt.xlable("Y axis")
