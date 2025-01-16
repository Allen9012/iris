import numpy as np

# 定义向量a和b；准确来说是一维数组
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 0])
# 计算向量内积
dot_product = np.dot(a, b)
# 打印内积
print("向量内积为：", dot_product)

# 定义矩阵 A 和 B
A = np.array([[1, 2, 10, 20], [3, 4, 30, 40]])
B = np.array([[1, 3], [2, 4], [10, 30], [20, 40]])
C = A @ B
print(C)
D = B @ A
print(D)


from numpy.random import randint
import time

num = 200
# num * num大小方阵，0~9随机数
A = randint(0, 10, size=(num, num))
B = randint(0, 10, size=(num, num))
# 使用NumPy计算矩阵乘法
start_time = time.time()  # 开始时刻
C_1 = A @ B
stop_time = time.time()  # 结束时刻
time_used = stop_time - start_time
print("--- %s seconds ---" % time_used)
C = np.zeros((num, num))
# num * num大小全0方阵
# 手动计算矩阵乘法
start_time = time.time()  # 开始时刻
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
time_used = stop_time - start_time
print("--- %s seconds ---" % time_used)
