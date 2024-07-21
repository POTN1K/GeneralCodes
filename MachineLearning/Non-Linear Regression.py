import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5.0, 5.0, 0.1)

# Quadratic
y = np.power(x, 2)
y_noise = 2 * np.random.normal(size=x.size)
ydata = y + y_noise
plt.plot(x, ydata,  'bo')
plt.plot(x, y, 'r')
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()

# Examples of how to plot non linear functions
# Exponential
Y = np.exp(X)

# Logarithmic
Y = np.log(X)

# Sigmoidal/ Logistic
Y = 1-4/(1+np.power(3, X-2))