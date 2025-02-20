# 自定义函数
def custom_meshgrid(x, y):
    num_x = len(x)
    num_y = len(y)
    X = []
    Y = []
    # 外层for循环
    for i in range(num_y):
        X_row = []
        Y_row = []
        # 内层for循环
        for j in range(num_x):
            X_row.append(x[j])
            Y_row.append(y[i])
        # 生成二维数组
        X.append(X_row)
        Y.append(Y_row)
    return X, Y


# 示例用法
x = [0, 1, 2, 3, 4, 5]  # 横坐标列表
y = [0, 1, 2, 3]  # 纵坐标列表
# 调用自定义函数
X, Y = custom_meshgrid(x, y)
print("X坐标：")
print(X)
print("Y坐标：")
print(Y)
