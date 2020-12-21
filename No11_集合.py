# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 {} 或者 set() 函数创建集合，注意：创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典。
# 集合会自动去重且无序
parame1 = {"apple", "blue", "people", "people"}
print(parame1)
parame2 = set("好好学习，天天向上！！！")
print(parame2)
# 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
parame1.add("look")
print(parame1)
# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
parame1.update(["a", "b"])
parame1.update([1, 2], [3,"gun"])
parame2.update({"name":"xiao"})
print(parame1)
print(parame2)
