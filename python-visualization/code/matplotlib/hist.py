import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X = np.random.randn(10000)
fig, ax = plt.subplots(1,2,figsize=(14,7))

# 直接用matplotlib中的hist函数绘制
ax[0].hist(X, bins=15,
        edgecolor='green',
        facecolor='cyan',
        linewidth=1,
        histtype='bar')
ax[0].set_title('hist()')

# 使用seaborn中的distplot函数绘制（包括拟合的概率密度曲线）
sns.set_palette("hls")  # 设置所有图的颜色，使用hls色彩空间
sns.distplot(X, color="r", bins=15, kde=True, ax=ax[1])
ax[1].set_title('sns.distplot()')

plt.savefig("hist.png", dpi=800)
plt.show()
