import numpy as np

# 定义迭代函数 φ(x) = e^(-x)，这是我们的方程 x = e^(-x) 的右侧
def phi(x):
    return np.exp(-x)

# Aitken加速法函数
def aitken_acceleration(x0, num_iterations):
    x = x0  # 设置初始迭代值 x0
    for _ in range(num_iterations):  # 进行指定次数的迭代
        x1 = phi(x)  # 计算 x1 = φ(x)
        x2 = phi(x1)  # 计算 x2 = φ(x1)
        # 应用Aitken加速公式
        x = x - (x1 - x)**2 / (x2 - 2*x1 + x)
    return x  # 返回最终加速后的结果

# 初始值和迭代次数
x0 = 0.5  # 初始迭代值
num_iterations_aitken = 3  # 迭代3次

# 执行Aitken加速法
root_aitken = aitken_acceleration(x0, num_iterations_aitken)

print("Aitken加速法求得的根:", root_aitken)
