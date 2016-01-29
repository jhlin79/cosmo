import numpy as np
import matplotlib.pyplot as plt
import sys

fn = sys.argv[1]
f = open(fn)
con = f.readlines()
r = []
xi = []
for line in con:
    l = line.split()
    r.append( float(l[0]) )
    xi.append( float(l[1]) )

r = np.array(r)
xi = np.array(xi)
plt.plot(r, xi*r**2)
plt.show()
