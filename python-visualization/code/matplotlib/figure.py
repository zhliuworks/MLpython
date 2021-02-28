import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.5,3.5,300)  # 在0.5到3.5之间均匀地取300个数
y = np.sin(x)
z = np.cos(x)

# fig, ax = plt.subplots(figsize=(14,7))  不设置子图
fig, ax = plt.subplots(1,2,figsize=(14,7))
ax[0].plot(x,y)
ax[1].plot(x,z)

ax[0].set_title('sin(x)', fontsize=18)
ax[1].set_title('cos(x)', fontsize=18)

ax[0].set_xlabel('x', fontsize=18, fontfamily = 'sans-serif', fontstyle='italic')
ax[1].set_xlabel('x', fontsize=18, fontfamily = 'sans-serif', fontstyle='italic')

ax[0].set_ylabel('y', fontsize='x-large',fontstyle='oblique')
ax[1].set_ylabel('y', fontsize='x-large',fontstyle='oblique')

ax[0].set_xlim(0,16)
ax[0].grid(axis='both')

ax[1].xaxis.set_tick_params(rotation=45, labelsize=12)
start, end = ax[1].get_xlim()
ax[1].xaxis.set_ticks(np.arange(start, end, 1))  # np.arange(start, end, step)
ax[1].yaxis.tick_right()

plt.savefig('figure.png', dpi=800)
plt.show()
