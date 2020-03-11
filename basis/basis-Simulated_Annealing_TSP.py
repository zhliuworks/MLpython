# Simulated Annealing Algorithm
import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

# TSP问题：北京、上海、广州、武汉、重庆、成都、厦门、昆明、西安、济南
city = ['北京', '上海', '广州', '武汉', '重庆', '成都', '厦门', '昆明', '西安', '济南']
dis = np.array([[0, 1328, 2267, 1200, 1936, 2001, 2287, 2982, 1159, 495],
                [1328, 0, 1532, 811, 1949, 2159, 1110, 2656, 1509, 968],
                [2267, 1532, 0, 1022, 1907, 2233, 850, 1637, 2176, 1998],
                [1200, 811, 1022, 0, 1159, 1289, 1175, 2034, 1025, 976],
                [1936, 1949, 1907, 1159, 0, 504, 2188, 1237, 790, 1837],
                [2001, 2159, 2233, 1289, 504, 0, 2471, 1100, 842, 1610],
                [2287, 1110, 850, 1175, 2188, 2471, 0, 2516, 2240, 1914],
                [2982, 2656, 1637, 2034, 1237, 1100, 2516, 0, 1942, 2978],
                [1159, 1509, 2176, 1025, 790, 842, 2240, 1942, 0, 1179],
                [495, 968, 1998, 976, 1837, 1610, 1914, 2978, 1179, 0]])


def total_dis(ord):
    total = 0
    for i in range(10):
        total += dis[ord[i], ord[(i + 1) % 10]]
    return total


temp_ini = 10  # 初始温度
rounds = 100000  # 迭代轮数
order = np.arange(10)
np.random.shuffle(order)
costs = np.zeros([rounds, 1])
temps = np.zeros_like(costs)

for t in trange(1, rounds + 1):
    temp = temp_ini / np.log10(1 + t)
    temps[t - 1] = temp
    a = np.random.randint(10)
    b = np.random.randint(10)
    while b == a:
        b = np.random.randint(10)

    new_order = np.copy(order)
    c = new_order[a]
    new_order[a] = new_order[b]
    new_order[b] = c

    cost = total_dis(order)
    new_cost = total_dis(new_order)
    costs[t - 1] = cost

    if new_cost < cost:
        order = new_order
    elif np.random.rand() < np.exp(-(new_cost - cost) / temp):
        order = new_order

i = 0
while order[i] != 4:
    i += 1
print(city[order[i]], end="")
for j in range(10):
    print(' -> ', city[order[(i + j + 1) % 10]], end="")

fig = plt.figure(figsize=(100, 200))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.scatter(np.arange(rounds), costs, color='blue', s=1)
ax2.scatter(np.arange(rounds), temps, color='red', s=1)
ax1.set_xlabel('Rounds')
ax2.set_xlabel('Rounds')
ax1.set_ylabel('Total Distance')
ax2.set_ylabel('Temperature')
plt.title('TSP Solution')
plt.show()