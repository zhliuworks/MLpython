import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.5,3.5,300)  # 在0.5到3.5之间均匀地取300个数
y = np.sin(x)

# 绘制曲线
plt.plot(x, y, color='blue', linestyle='-', linewidth=1, marker='o', markersize=4, label='Line')

# 其他属性设置
# 坐标轴范围
plt.xlim(1,3)              # x轴范围
plt.ylim(min(y),max(y))    # y轴范围

# 坐标轴坐标数标签
# 第一个参数为欲替换的x坐标，第二个参数为对应替换坐标的标签
plt.xticks([0,2,4,6,8],[1,2,'a',4,5])
# 也可以直接给出坐标数组
plt.yticks(np.linspace(-1,1,20))

# 坐标轴标签
plt.xlabel('time', fontname='Times New Roman', fontsize=10)
plt.ylabel('value')

# 图片标题
plt.title('plot')

# 图例显示
# loc--位置（1:右上，2：左上，3：左下，4：右下）
plt.legend(loc=1)

# 网格线开关
plt.grid(axis="x")
plt.grid(axis="y")

# 保存图片
plt.savefig('plot.png', dpi=800)

# 显示图片
plt.show()
