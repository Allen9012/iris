def list1():
    # 创建一个混合列表
    my_list = [1, 1.0, "1", True, [1, 1.0, "1"], {1}, {1: 1.0}]
    print("列表长度为")
    print(len(my_list))
    # 打印每个元素和对应的序号
    for index, item in enumerate(my_list):
        type_i = type(item)
    print(f"元素：{item}，索引：{index}，类型：{type_i}")
    # 列表索引
    print(my_list[0])
    print(my_list[1])
    print(my_list[-1])
    print(my_list[-2])
    # 列表切片
    # 取出前3个元素，索引为0、1、2
    print(my_list[:3])
    # 取出索引1、2、3，不含0，不含4
    print(my_list[1:4])
    # 指定步长2，取出第0、2、4、6
    print(my_list[::2])
    # 指定步长-1，倒序
    print(my_list[::-1])
    # 提取列表中的列表某个元素
    print(my_list[4][1])


def list2():
    # 创建一个混合列表
    my_list = [1, 1.0, "12ab", True, [1, 1.0, "1"], {1}, {1: 1.0}]
    print(my_list)
    # 修改某个元素
    my_list[2] = "123"
    print(my_list)
    # 在列表指定位置插入元素
    my_list.insert(2, "inserted")
    print(my_list)
    # 在列表尾部插入元素
    my_list.append("tail")
    print(my_list)
    # 通过索引删除
    del my_list[-1]
    print(my_list)
    # 删除某个元素
    my_list.remove("123")
    print(my_list)
    # 判断一个元素是否在列表中
    if "123" in my_list:
        print("Yes")
    else:
        print("No")
    # 列表翻转
    my_list.reverse()
    print(my_list)
    # 将列表用所有字符连接，连接符为下划线 _
    letters = ["J", "a", "m", "e", "s"]
    word = "_".join(letters)
    print(word)


def combined_list():
    # 定义列表
    list_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    first, *list_rest = list_0
    print(list_rest)  # [1, 2, 3, 4, 5, 6, 7, 8]
    first, second, *list_rest = list_0
    print(list_rest)  # [2, 3, 4, 5, 6, 7, 8]
    first, second, *list_rest, last = list_0
    print(list_rest)  # [2, 3, 4, 5, 6, 7]
    first, *list_rest, _ = list_0
    print(list_rest)  # [1, 2, 3, 4, 5, 6, 7]
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8]
    # 合并
    combined_list = [list1, list2]
    combined_list2 = [*list1, *list2]
    print(combined_list)  # [1, 2, 3, 4, 5, 6, 7, 8]
    print(combined_list2)  # [[1, 2, 3, 4, 5], [6, 7, 8]]


def combined_strlist():
    # 定义字符串
    string_0 = "abcd"
    first, *str_rest, last = string_0
    print(str_rest)  # ['b', 'c']
    # 定义元组
    tuple_0 = (1, 2, 3, 4)
    first, *tuple_rest, last = tuple_0
    print(tuple_rest)  # [2, 3]


# combined_list()
combined_strlist()
