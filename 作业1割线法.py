import math

# 定义方程函数 f(x)
def f(x):
    return x * math.exp(x) - 1

# 割线法函数
def secant_method(x0, x1, iterations):
    for i in range(iterations):
        # 计算下一个近似根 x2
        x2 = x1 - ((x1 - x0) / (x1 * math.exp(x1) - x0 * math.exp(x0))) * (x1 * math.exp(x1) - 1)

        # 打印每次迭代的结果
        print(f"Iteration {i + 1}: x{i + 2} = {x2}")

        # 更新 x0 和 x1 的值
        x0, x1 = x1, x2

    # 返回最终的近似根 x2
    return x2

# 设置初始近似根值和迭代次数
initial_x0 = 0.5
initial_x1 = 0.6
num_iterations = 4

# 调用割线法函数并得到最终的近似根
root = secant_method(initial_x0, initial_x1, num_iterations)

# 打印最终结果
print(f"Root after {num_iterations} iterations: x = {root}")
