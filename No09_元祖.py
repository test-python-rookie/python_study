def jichu():
    # 元祖跟字符串类似
    # 元祖不可改
    # 元祖用()表示，用“,”分隔
    tuple1 = (3, 5, 9, 2, 1, 3)
    # 统计
    print(tuple1.count(3))
    # 求最大
    print(max(tuple1))
    # 求最小
    print(min(tuple1))
    # 长度
    print(len(tuple1))
    # 列表转为元祖
    list = [3, 3, 9, 9, 1, 3]
    tuple2 = tuple(list)
    print(tuple2)

if __name__ == '__main__':
    jichu()
