# 8.2str类
# 通过str创建的字符串对象是不可变的
s1 = str("hello world")
print(s1)
s2 = "hello world"
print(s1)
print(id(s1), id(s2))
# 具有相同内容的字符串实际上是同一个对象
print(max(s1))
# 返回s1中ASCII码最大的字符
print(min(s1))
# 返回s1中ASCII码最小的字符
print(s1[1:3])
# 截取s1中下表从1到3(不含)的子串，[:]则默认为从零开始到最后一个下表
print("hello" in s1)
print("ask" not in s1)
# 字面含义
# 比较字符串，按顺序以ASCII码大小比较
# 迭代字符串的两种方法
for ch in s1:
    print(ch)
for i in range(0, len(s1)):
    print(s1[i])
# 测试字符串
print(s1.isalnum())
print(s1.isalpha())
print(s1.isdigit())
print(s1.islower())
print(s1.isupper())
print(s1.isspace())
# 搜索子串
print(s1.endswith("world"))
# 是否以特定结尾
print(s1.startswith("world"))
# 是否以特定开头
print(s1.find("h"))
# 返回下标，不存在则返回-1
print(s1.find("h"))
# 从右侧查找
print(s1.count("l"))
# 出现次数
# 转换字符串
#删除字符串中的空格
#格式化字符串