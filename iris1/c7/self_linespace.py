# 自定义函数模仿 numpy.linspace()
# 二维线图时，经常会使用 numpy.linspace() 生成颗粒度高的等差数列。
def linspace(start, stop, num=50, endpoint=True):
    if num < 2:
        # 报错
        raise ValueError("Number of samples must be at least 2")
    # 是否包括右端点
    if endpoint:
        step = (stop - start) / (num - 1)
        return [start + i * step for i in range(num)]
    else:
        step = (stop - start) / num
        return [start + i * step for i in range(num)]


# 示例用法
start = 0  # 数列起点
stop = 10  # 数列终点
num = 21  # 数列元素
endpoint = True  # 数列包含 stop
# 调用自定义函数生成等差数列
values = linspace(start, stop, num, endpoint)
