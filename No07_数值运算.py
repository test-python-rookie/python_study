def jichu():
    a, b = 5, 3
    print("加：%d + %d = %d"%(a, b, a+b))
    print("减：%d - %d = %d"%(a, b, a-b))
    print("乘：%d * %d = %d"%(a, b, a*b))
    # %d带符号的整数，%g浮点数字(根据值的大小采用%e或%f)，%s字符串
    print("除，得到一个浮点数：%d / %d = %g"%(a, b, a/b))
    print("除，得到一个整数：%d // %d = %d"%(a, b, a//b))
    print("取余：%d"%a + " % " + "%d = %d"%(b, a%b))
    print("乘方：%d ** %d = %d"%(a, b, a**b))

# 例子
# 九九乘法表
def lizi():
    for i in range(1, 10):
        for j in range(1, i + 1):
            num = j * i
            print("%d * %d = %d"%(j, i, num), end="\t")
        print()


if __name__ == '__main__':
    lizi()

