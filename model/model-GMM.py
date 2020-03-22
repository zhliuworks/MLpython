# Gaussian Mixture Model with Iris
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from tqdm import trange


# 多维高斯分布密度函数
def normal_density(x, mu, sig, dim):
    diff = x - mu
    tmp = np.matmul(diff.transpose(), np.linalg.inv(sig))
    tmp = np.matmul(tmp, diff)
    tmp = np.exp(-0.5 * tmp)
    coef = np.power(2 * np.pi, -0.5 * dim) * np.power(np.linalg.det(sig), -0.5)
    return coef * tmp


# 0.数据加载
iris = datasets.load_iris()
X = MinMaxScaler().fit_transform(iris.data)  # (150,4)
y = iris.target.reshape(-1, 1)  # 由于GMM为无监督学习，不利用y作为标记，最终用来检验聚类效果

# 1.初始化
mu = np.array([[np.random.rand(), np.random.rand(), np.random.rand()],
               [np.random.rand(), np.random.rand(), np.random.rand()],
               [np.random.rand(), np.random.rand(), np.random.rand()],
               [np.random.rand(), np.random.rand(), np.random.rand()]])
sig = np.zeros((3, 4, 4))
sig[0, ...] = np.eye(4)
sig[1, ...] = np.eye(4)
sig[2, ...] = np.eye(4)
pi = np.array([1 / 3, 1 / 3, 1 / 3])
gamma = np.zeros((150, 3))

# 2.EM algorithm 求解
for n in trange(1000):
    # E-Step: 计算每个点归属每个类的概率
    for i in range(150):
        total = 0
        for k in range(3):
            gamma[i, k] = pi[k] * normal_density(x=X[i, ...].transpose(), mu=mu[..., k], sig=sig[k, ...], dim=4)
            total += gamma[i, k]
        for k in range(3):
            gamma[i, k] = gamma[i, k] / total

    # M-Step:重新计算先验概率pi、均值mu、协方差sig
    total = 0
    for k in range(3):
        pi[k] = 0
        for i in range(150):
            pi[k] += gamma[i, k]
        total += pi[k]

    for k in range(3):
        mu[..., k] = np.zeros_like(mu[..., k])
        for i in range(150):
            mu[..., k] += gamma[i, k] * X[i, ...]
        mu[..., k] /= pi[k]

        sig[k, ...] = np.zeros_like(sig[k, ...])
        for i in range(150):
            diff = X[i, ...] - mu[..., k]
            diff = diff.reshape(-1, 1)
            sig[k, ...] += gamma[i, k] * np.matmul(diff, diff.transpose())
        sig[k, ...] /= pi[k]

        pi[k] /= total

clus = np.zeros((150, 1))
for i in range(150):
    clus[i, 0] = int(np.argmax(gamma[i, ...]))

acc = 0
temp = np.zeros(3)
for i in range(0, 50):
    temp[int(clus[i, 0])] += 1
acc += max(temp)
temp = np.zeros(3)
for i in range(50, 100):
    temp[int(clus[i, 0])] += 1
acc += max(temp)
temp = np.zeros(3)
for i in range(100, 150):
    temp[int(clus[i, 0])] += 1
acc += max(temp)

acc /= 150
print(acc)
