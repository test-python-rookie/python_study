# 定义字符串
str = "abcdefg"
# 显示完整字符串
print(str)
# 显示第2个到第4个字符（下标从0开始，包头不包尾）
print(str[1:4])
# 显示第3个到最后一个字符
print(str[2:])
# 显示倒数第一个字符
print(str[-1])
# 显示从第二个开始到第五个且每隔两个的字符
print(str[0:5:2])
# 显示字符串两次
print(str * 2)
# 字符串拼接
print(str + 'dong')
# 加“\”转译（\n：换行）
print("abc\ndef")
# 加“r”取消转译
print(r"abc\ndef")

# 例子
# 敏感词替换
st = "我反共，反中国，我是坏人，我造反，啦啦啦"
newst1 = st.replace("反共", "**").replace("反中", "爱中").replace("坏", "好")
# 替换次数
newst2 = st.replace("反", "爱", 2)
print(newst1)
print(newst2)




