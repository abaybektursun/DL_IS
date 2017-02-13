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