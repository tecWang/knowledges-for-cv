# 可以采用牛顿迭代公式求一个数的平方根与立方根

n = float(input())
x = 1.0
temp = pow(x, 3)

# 牛顿迭代法更新公式:
#   x = x_0 - \frac{ f(x_0) }{ f'(x_0) }
#       如果是平方根公式：f(x) = x^2 - A
#       如果是立方根公式: f(x) = x^3 - A
#       求导代入不同公式即可求解
while abs(temp - n) > 0.001:
    x = x - (temp - n) / (3*pow(x, 2))
    temp = pow(x, 3)
    print("x", x)
print("{:.1f}".format(x))