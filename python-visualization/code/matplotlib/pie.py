import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))
colors = ["#e41a1c","#377eb8","#4daf4a","#984ea3"]
soldNums = [0.05,0.45,0.15,0.35]
kinds = ['case1','case2','case3','case4']

plt.pie(soldNums,
       labels=kinds,
       autopct="%.2f%%", # 保留两位小数
       startangle=0,  # 起始角度
       colors=colors);

plt.savefig('pie.png', dpi=800)
plt.show()
