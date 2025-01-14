import copy

a = [1, 2, 3]
b = a
# 视图 b 引用 a 的内存地址
c = [1, 2, 3]
d = a.copy()
print(a is b)
# 输出 True，因为 a 和 b 引用同一个内存地址
print(a is not c)
# 输出 True，因为 a 和 c 引用不同的内存地址
print(a == c)
# 输出 True，因为 a 和 c 的值相等
print(a is not d)
# 输出 True，因为 a 和 d 引用不同的内存地址
print(a == d)
# 输出 True，因为 a 和 d 的值相等
a_2_layers = [1, 2, [3, 4]]
d_2_layers = a_2_layers.copy()
e_2_layers = copy.deepcopy(a_2_layers)
print(a_2_layers is d_2_layers)
print(a_2_layers[2] is d_2_layers[2])  # 请特别关注!
print(a_2_layers is e_2_layers)
print(a_2_layers[2] is e_2_layers[2])
