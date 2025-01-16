import random
import statistics
import matplotlib.pyplot as plt

random.seed(0)

# 抛骰子实验的次数
num_flips = 1000

dice_array = [1, 2, 3, 4, 5, 6]
mean_array = []
rst_array = []
for _ in range(num_flips):
    rst = random.choice(dice_array)
    rst_array.append(rst)
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

plt.xlabel("Number of dice flips")
plt.ylabel("Result")
plt.grid(True)
plt.show()

# 可视化均值随次数变化
plt.plot(range(1, num_flips + 1), mean_array)
plt.axhline(3, color="r")
plt.xlabel("Number of coin flips")
plt.ylabel("Running Mean")
plt.grid(True)
plt.ylim(0, 6)
plt.show()
