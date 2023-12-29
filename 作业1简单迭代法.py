import math  # 导入数学库

def phi(x):  # 定义函数phi(x)，表示迭代公式x=e^(-x)
    return math.exp(-x)  # 返回e的-x次幂，即e^(-x)

def simple_iterate(initial_x, iterations):  # 定义简单迭代函数simple_iterate，接收初始值和迭代次数作为参数
    x = initial_x  # 设定初始值x为传入的初始值参数
    for i in range(iterations):  # 使用for循环进行迭代，迭代次数由传入的iterations参数确定
        x = phi(x)  # 使用定义的phi函数进行迭代计算，得到新的x值
        print(f"Iteration {i + 1}: x = {x}")  # 打印每次迭代后的x值
    return x  # 返回最终迭代后的x值

initial_value = 0.5  # 设定初始值为0.5
num_iterations = 14  # 设定迭代次数为14次

result = simple_iterate(initial_value, num_iterations)  # 调用simple_iterate函数进行迭代计算
print(f"Result after {num_iterations} iterations: x = {result}")  # 打印迭代后的结果
