# 列表跟字符串类似，不过列表可以修改
# 列表用[]代表，其中的元素用“,”隔开
def lichu():
    # 一个列表的元素可以各不相同
    list = [1, "12", 1.1, [1, 2]]
    print(type(list[0]), type(list[1]), type(list[2]), type(list[3]))
    print(list[0], list[1], list[2], list[3])
    # 修改列表
    list[2] = 5
    print(list)
    list[1:3] = [5, 9]
    print(list)
    # 删除列表中的元素
    del list[3]
    print(list)
    # 迭代
    for i in list:
        print(i, end=" ")
# 例子
# 排除特定数字
def paichu():
    list = [2, 4, 9]
    for i in range(10):
        if i in list:
            continue
        else:
            print(i)
# 冒泡算法
def maopao():
    list = [10,9,8,7,6,5,4]
    n = len(list)
    for j in range(n):
        for i in range(n - 1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                # print(list)
        n -= 1
    print(list)

if __name__ == '__main__':
    maopao()
