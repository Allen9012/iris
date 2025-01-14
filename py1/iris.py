# 导入包
from sklearn.datasets import load_iris

# 使用load_iris函数加载Iris数据集
iris = load_iris()
# Iris数据集的特征存储在iris.data中
X = iris.data
print(type(X))  # numpy.ndarray
# Iris数据集的目标（标签）存储在iris.target中
y = iris.target
print(type(y))  # numpy.ndarray

# 导入包
import seaborn as sns

# 使用seaborn.load_dataset函数加载Iris数据集
iris_df = sns.load_dataset("iris")
# 查看数据集的前5行
iris_df.head()
print(type(iris_df))  # pandas.core.frame.DataFrame
