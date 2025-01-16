import random
import statistics
import matplotlib.pyplot as plt

random.seed(0)

# 抛骰子实验的次数
num_flips = 1000
dice_array = [1, 2, 3, 4, 5, 6]
probabilities = [0.2, 0.16, 0.16, 0.16, 0.16, 0.16]


def roll_uneven_dice():
    return random.choices(dice_array, probabilities)[0]


# 进行实验
results = []
means = []
for i in range(1, num_flips + 1):
    results.append(roll_uneven_dice())
    means.append(statistics.mean(results))

# 可视化
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_flips + 1), means, label="mean val")
# 计算理论期望值：E = Σ(p_i * x_i)
expected_value = sum(p * v for p, v in zip(probabilities, dice_array))
plt.axhline(
    y=expected_value,
    color="r",
    linestyle="--",
    label="theoretical value",
)
plt.xlabel("dice num")
plt.ylabel("mean")
plt.title("dice change with times")
plt.legend()
plt.grid(True)
plt.show()
