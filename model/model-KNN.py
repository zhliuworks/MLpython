# KNN Algorithm
from sklearn import datasets  # 导入内置数据集
from sklearn.neighbors import KNeighborsClassifier  # 导入KNN分类器
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler  # 归一化
from sklearn.metrics import confusion_matrix, accuracy_score  # 混淆矩阵，精确度

train_size = 0.8
k = 5

iris = datasets.load_iris()
X = MinMaxScaler().fit_transform(iris.data)  # 150*4矩阵，对每列min-max归一化
y = iris.target  # 150向量，包括0，1，2三类
train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=train_size, test_size=1 - train_size)
model = KNeighborsClassifier(n_neighbors=k)
model.fit(train_X, train_y)
y_pred = model.predict(test_X)

# 混淆矩阵：以实际类别为行，预测类别为列，衡量误差的可视化工具，一般用于监督学习
cnf_mat = confusion_matrix(test_y, y_pred)
print(cnf_mat)
print(accuracy_score(test_y, y_pred))

# 该方法也可用于手写数字识别
