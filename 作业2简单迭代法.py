import numpy as np

# 定义迭代函数 φ(x) = e^(-x)，这是我们的方程 x = e^(-x) 的右侧
def phi(x):
    return np.exp(-x)

# 简单迭代法函数
def simple_iteration(x0, num_iterations):
    x = x0  # 设置初始迭代值 x0
    for _ in range(num_iterations):  # 进行指定次数的迭代
        x = phi(x)  # 更新 x 的值为 φ(x)
    return x  # 返回最终迭代后的结果

# 初始值和迭代次数
x0 = 0.5  # 初始迭代值
num_iterations_simple = 14  # 迭代14次

# 执行简单迭代法
root_simple = simple_iteration(x0, num_iterations_simple)

print("简单迭代法求得的根:", root_simple)
