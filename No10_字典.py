# 键值唯一
# 键值不能为列表
# 例子
def lizi():
    n = int(input("请输入学生数量："))
    list = []
    for i in range(n):
        j = i + 1
        name = input("请输入第%d个学生姓名："%j)
        sex = input("请输入第%d个学生性别："%j)
        age = input("请输入第%d个学生年龄："%j)
        dict = {'姓名':name, '性别':sex, '年龄':age}
        list.append(dict)
        # print("姓名：%s，性别：%s，年龄：%s"%(dict['姓名'], dict['性别'], dict['年龄']))
    for i in range(n):
        # print(list[i])
        dict1 = list[i]
        print("姓名：%s，性别：%s，年龄：%s" % (dict1['姓名'], dict1['性别'], dict1['年龄']))


if __name__ == '__main__':
    lizi()