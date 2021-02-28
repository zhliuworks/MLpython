import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [3,1,4,5,8,9,7,2]

fig, ax = plt.subplots(1,2,figsize=(14,7))
ax[0].bar(x,y,
        align='center',
        color='c',
        tick_label = ['A','B','C','D','E','F','G','H'])
ax[0].set_xlabel('Container No.')
ax[0].set_ylabel('Weight (kg)')
ax[0].set_title('bar')
ax[0].grid(axis='y')

ax[1].barh(x,y,
        align='center',
        color='m',
        tick_label = ['A','B','C','D','E','F','G','H'])
ax[1].set_ylabel('Container No.')
ax[1].set_xlabel('Weight (kg)')
ax[1].set_title('barh')
ax[1].grid(axis='x')

plt.savefig('bar.png', dpi=800)
plt.show()
