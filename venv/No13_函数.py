# 不可变对象
def no(a):
    a = 3
    print("函数内取值1：地址：", id(a),"值：", a)
a = 1
print("函数外取值1：地址：", id(a),"值：", a)
no(a)
print("函数外取值2：地址：", id(a),"值：", a)

# 可变对象
def yes(list):
    list.append(4)
    print("函数内取值2：地址：", id(list),"值：", list)
list = [1, 2, 3]
print("函数外取值3：地址：", id(list),"值：", list)
yes(list)
print("函数外取值4：地址：", id(list),"值：", list)