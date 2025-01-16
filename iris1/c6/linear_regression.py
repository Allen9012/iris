# 导入包
import random
import statistics
import matplotlib.pyplot as plt

# 产生数据
num = 50
random.seed(0)
x_data = [random.uniform(0, 10) for _ in range(num)]
# 噪音
noise = [random.gauss(0, 1) for _ in range(num)]
y_data = [0.5 * x_data[idx] + 1 + noise[idx] for idx in range(num)]

# # 绘制散点图
# fig, ax = plt.subplots()  # 利用 plt.subplots() 产生图形对象 fig、轴对象 ax。
# ax.scatter(x_data, y_data)
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_aspect("equal", adjustable="box")  # 设置轴对象 ax 的纵横比例为相等。
# ax.set_xlim(0, 10)
# ax.set_ylim(-2, 8)
# ax.grid()

# 一元线性回归
slope, intercept = statistics.linear_regression(
    x_data, y_data
)  # 一元线性回归的斜率和截距

# 生成一个等差数列
start, end, step = 0, 10, 0.5
x_array = []
x_i = start
while x_i <= end:
    x_array.append(x_i)
    x_i += step
# 计算x_array预测值
y_array_predicted = [slope * x_i + intercept for x_i in x_array]

# 可视化一元线性回归直线
fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.plot(x_array, y_array_predicted, color="r")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(0, 10)
ax.set_ylim(-2, 8)
ax.grid()

plt.show()
