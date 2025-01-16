import random
import statistics
import matplotlib.pyplot as plt

# 抛硬币实验的次数
num_flips = 1000

coin_count = 0
# 用于存储每次抛硬币的结果
rst_array = []
# 用于存储每次抛硬币后的均值
mean_array = []
for _ in range(num_flips):
    # 随机抛硬币，1代表正面 (H)，0代表反面 (T)
    result_idx = random.randint(0, 1)
    rst_array.append(result_idx)
    # 计算当前所有结果的均值
    mean_idx = statistics.mean(rst_array)
    mean_array.append(mean_idx)

# 可视化前100次结果均值随次数变化
visual_num = 100
plt.scatter(
    range(1, visual_num + 1),
    rst_array[0:visual_num],
    c=rst_array[0:visual_num],
    marker="o",
    cmap="cool",
)
plt.plot(range(1, visual_num + 1), rst_array[0:visual_num])

plt.xlabel("Number of coin flips")
plt.ylabel("Result")
plt.grid(True)
plt.show()

# 可视化均值随次数变化
plt.plot(range(1, num_flips + 1), mean_array)
plt.axhline(0.5, color="r")
plt.xlabel("Number of coin flips")
plt.ylabel("Running Mean")
plt.grid(True)
plt.ylim(0, 1)
plt.show()
