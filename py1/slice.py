greeting_str = "Hey, James!"
# 打印字符串长度
print("字符串的长度为：")
print(len(greeting_str))
# 打印每个字符和对应的索引
for index, char in enumerate(greeting_str):
    print(f"字符：{char}，索引：{index}")
# 单个字符索引
print(greeting_str[0])
print(greeting_str[1])
print(greeting_str[-1])
print(greeting_str[-2])
# 切片
# 取出前3个字符，索引为0、1、2
print(greeting_str[:3])
# 取出索引1、2、3、4、5，不含0，不含6
print(greeting_str[1:6])
# 指定步长2，取出第0、2、4 ...
print(greeting_str[::2])
# 指定步长-1，倒序
print(greeting_str[::-1])
