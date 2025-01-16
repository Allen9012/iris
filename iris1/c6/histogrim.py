import random
import statistics
import matplotlib.pyplot as plt

random.seed(0)  # 方便复刻结果
# 生成300个服从N(0, 1**2)的随机数   mean1 是正态分布的均值。  std1 是正态分布的标准差。
mean1, std1, size1 = 0, 1, 300
data1 = [random.gauss(mean1, std1) for _ in range(size1)]

# 生成700个服从N(10, 5**2)的随机数
mean2, std2, size2 = 10, 5, 700
data2 = [random.gauss(mean2, std2) for _ in range(size2)]

# 将两组随机数混合
mixed_data = data1 + data2
mean_loc = statistics.mean(mixed_data)
std_loc = statistics.stdev(mixed_data)

# 绘制混合数据的直方图
plt.hist(
    mixed_data,
    bins=30,  # 区间
    density=True,
    edgecolor="black",
    alpha=0.7,
    color="blue",
    label="Mixed data",
)
plt.axvline(mean_loc, color="red", label="Mean")
plt.axvline(mean_loc + std_loc, color="pink", label="Mean ± std")
plt.axvline(mean_loc - std_loc, color="pink")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.title("Histogram of Mixed Data")
plt.grid(True)
plt.show()
