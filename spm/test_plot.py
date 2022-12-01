import os
import numpy as np
import matplotlib.pyplot as plt
import spm1d

# load plain-text data (30 rows, 100 columns):
dir0         = os.path.dirname(__file__)
# fname        = os.path.join(dir0, 'data', 'ex_kinematics.txt')
fname        = os.path.join(dir0, 'test_2.txt')
Y            = np.loadtxt(fname)   #30 curves, 100 nodes
# print(Y)
L = Y[0:100,0]
M = Y[0:100,1]
N = Y[0:100,2]
# print(M)
print(Y.shape)

# plot:
plt.close('all')
fig,AX = plt.subplots( 1, 3, figsize=(12, 3.5) )

# plt.subplot(1, 2, 1)
# plt.subplot(1, 2, 1)
# ax     = AX[0]
# plt.plot(Y, color = 'k')
# plt.xlabel('Time (%)', size=20)
# plt.ylabel(r'$\theta$ (deg)', size=20)

ax     = AX[0]
plt.sca(ax)
# spm1d.plot.plot_mean_sd(Y.T)
# spm1d.plot.plot_mean_sd(Y, linecolor='r', facecolor='r')
# spm1d.plot.plot_mean_sd(M.T, linecolor='b', facecolor=(0.7,0.7,1), edgecolor='b', label='Slow')
plt.plot(L, color = 'k')
plt.ylim((-40,40))

ax     = AX[1]
plt.sca(ax)
plt.plot(M, color = 'b')
plt.ylim((-30,120))

ax     = AX[2]
plt.sca(ax)
plt.plot(N, color = 'r')
plt.ylim((-60,70))

plt.tight_layout()
plt.show()