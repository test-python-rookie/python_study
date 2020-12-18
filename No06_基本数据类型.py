# 赋相同值
a = b = c = "天才"
print(a,b,c)
# 赋不同值
e,f,g = 1,"dong",3.5
print(e,f,g)
'''
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
'''
# 查询变量所指的对象类型
print(type(a),type(e),type(f),type(g))
# 此外还可以用 isinstance 来判断
print(isinstance(g, int),isinstance(g, float))

