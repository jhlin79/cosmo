from astroML.correlation import two_point
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

c = np.array([[], [], []])
N = 500
offset = 60.0
noise = 3.0
BAO = 20.0

for i in xrange(100):
    N1 = np.random.randint(N/10.0, N)
    N2 = np.random.randint(N/10.0, N)
    r1 = (np.random.random(N1)-0.5)*noise* np.random.random()
    r2 = BAO + (np.random.random(N2)-0.5)*noise* np.random.random()
    x_off = 2*offset*(np.random.random() - 0.5)
    y_off = 2*offset*(np.random.random() - 0.5)
    z_off = 2*offset*(np.random.random() - 0.5)
    theta1 = np.random.random(N1) * np.pi
    phi1 = np.random.random(N1) * 2 * np.pi
    c1 = np.vstack( (r1*np.sin(theta1)*np.cos(phi1)+x_off, r1*np.sin(theta1)*np.sin(phi1)+y_off, r1*np.cos(theta1)+z_off ))
    theta2 = np.random.random(N2) * np.pi
    phi2 = np.random.random(N2) * 2 * np.pi
    c2 = np.vstack( (r2*np.sin(theta2)*np.cos(phi2)+x_off, r2*np.sin(theta2)*np.sin(phi2)+y_off, r2*np.cos(theta2)+z_off ))
    c = np.hstack( (c,c1,c2) )


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
np.random.shuffle(c)
ax.scatter(c[0][:], c[1][:], c[2][:])
plt.show()
cor = two_point(c.T, np.linspace(int(BAO)/10.0, int(BAO)*2, int(BAO)*2), method='landy-szalay')
plt.plot(cor)
plt.show()
