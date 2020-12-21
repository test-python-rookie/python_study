# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# 1,1,2,3,5,8,13...
a, b = 0, 1
i = 0
while b < 1000:
    print(b, end="")
    a, b = b, a + b
    i += 1
    if i % 5 == 0:
        print()
    else:
        print(end=",")

