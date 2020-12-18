# 键值唯一
# 键值不能为列表
# 例子
def lizi():
    name = input("请输入姓名：")
    sex = input("请输入性别：")
    age = input("请输入年龄：")
    dict = {'姓名':name, '性别':sex, '年龄':age}
    print("姓名：%s，性别：%s，年龄：%s"%(dict['姓名'], dict['性别'], dict['年龄']))


if __name__ == '__main__':
    lizi()