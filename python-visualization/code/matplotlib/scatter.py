import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#导入数据集
df = pd.read_csv("scatter_data.csv")
#拆分不同性别对应数据
mdf = df.query("sex=='m'")
fdf = df.query("sex=='f'")
#绘制男性数据
ax = mdf.plot.scatter(x='ageYear', y='heightIn', c='b', s=10, label='male')
#绘制女性数据
fdf.plot.scatter(x='ageYear', y='heightIn', c='r', s=30, label='female', ax=ax)
#取题目
ax.set_title('scatter')
#保存图片
plt.savefig('scatter.png', dpi=800)
#显示绘图结果
plt.show()
