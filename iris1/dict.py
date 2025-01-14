# 使用大括号创建字典
person = {"name": "James", "age": 88, "gender": "male"}
# 使用 dict() 函数创建字典
fruits = dict(apple=88, banana=888, cherry=8888)
# 访问字典中的值
print(person["name"])
print(fruits["cherry"])
# 修改字典中的值
person["age"] = 28
print(person)
# 添加键值对
person["city"] = "Toronto"
print(person)
# 删除键值对
del person["gender"]
print(person)
# 获取键、值、键值对列表
print(person.keys())
print(person.values())
print(person.items())
