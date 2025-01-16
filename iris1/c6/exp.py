import matplotlib.pyplot as plt
import math


# 定义函数 f(x) = exp(x)
def f(x):
    return math.exp(x)


# 生成 x 的取值范围，从 -3 到 3，步长为 0.1
x_values = [i * 0.1 for i in range(-30, 31)]
y_values = []

# 计算对应的 y 值
for x in x_values:
    y_values.append(f(x))

# 绘制图像
plt.plot(x_values, y_values)
plt.title("Graph of f(x) = exp(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
