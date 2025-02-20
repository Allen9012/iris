import copy


def view():
    list1 = [1, 2, 3, 4]
    # 赋值，视图
    list2 = list1
    # 拷贝，副本 (浅拷贝)  浅复制 (shallow copy) 只对 list 的第一层元素完成拷贝，深层元素还是和原 list 共用。
    list3 = list1.copy()
    list2[0] = "a"
    list2[1] = "b"
    list3[2] = "c"
    list3[3] = "d"
    print(list1)
    print(list2)
    print(list3)


def deep_copy():
    list1 = [1, 2, 3, [4, 5]]
    print("原始list")
    print(list1)
    # 深复制，适用于嵌套列表
    list_deep = copy.deepcopy(list1)
    # 只拷贝一层
    list2 = list1.copy()
    list3 = list1[:]
    list4 = list(list1)
    list5 = [*list1]
    # 修改元素
    list_deep[3][0] = "deep"
    list_deep[2] = "worked_0"
    list2[3][0] = "abc"
    list2[2] = "worked_1"
    list3[3][0] = "X1"
    list3[2] = "worked_2"
    list4[3][0] = "X2"
    list4[2] = "worked_3"
    list5[3][0] = "X3"
    list5[2] = "worked_4"
    print("新list")
    print(list1)
    print(list_deep)
    print(list2)
    print(list3)
    print(list4)
    print(list5)


# view()
deep_copy()
