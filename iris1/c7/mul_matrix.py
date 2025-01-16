# 定义矩阵 A 和 B
A = [[1, 2, 10, 20], [3, 4, 30, 40], [5, 6, 50, 60]]
B = [[4, 2], [3, 1], [40, 20], [30, 10]]
# 定义全 0 矩阵 C 用来存放结果
C = [[0, 0], [0, 0], [0, 0]]
# 矩阵乘法
# 遍历 A 的行
for i in range(len(A)):  # len(A) 给出 A 的行数
    # 遍历 B 的列
    for j in range(len(B[0])):
        # len(B[0]) 给出 B 的列数
        # 这一层相当于消去 k 所在的维度，即压缩
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
        # 完成对应元素相乘，再求和
# 输出结果
for row in C:
    print(row)