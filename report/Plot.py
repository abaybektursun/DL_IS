import prettyplotlib as ppl
import numpy as np

# prettyplotlib imports 
import matplotlib.pyplot as plt
import matplotlib as mpl
from prettyplotlib import brewer2mpl

fig, ax = plt.subplots(1)

x = np.arange(-2, 2, 0.1);
y = (1/2)*x**2

dfdx = x

ppl.plot(ax, x, y, label='f(x)', linewidth=0.75)
ppl.plot(ax, x, dfdx, label='f\'(x)', linewidth=0.75)

ppl.legend(ax, loc='lower right')

fig.savefig('gradient_descent.png')

#-----------------------------------------------------------------------------

# Set limits and number of points in grid
y, x = np.mgrid[10:-10:100j, 10:-10:100j]

x_obstacle, y_obstacle = 0.0, 0.0
alpha_obstacle, a_obstacle, b_obstacle = 1.0, 1e3, 2e3

p = x**2 - x*y

dy, dx = np.gradient(p, np.diff(y[:2, 0]), np.diff(x[0, :2]))

skip = (slice(None, None, 3), slice(None, None, 3))

fig, ax = plt.subplots()
im = ax.imshow(p, extent=[x.min(), x.max(), y.min(), y.max()])
ax.quiver(x[skip], y[skip], dx[skip], dy[skip])

fig.colorbar(im)
ax.set(aspect=1, title='')
#plt.show()

fig.savefig('Quiver.png')
