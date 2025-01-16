# 计算向量内积
# 定义向量a和b
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0]
# 初始化内积为0
dot_product = 0
# 使用for循环计算内积
for a_i, b_i in zip(a, b):
    dot_product += a_i * b_i
# 打印内积
print("向量内积为：", dot_product)
