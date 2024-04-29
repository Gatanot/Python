# 3.2 常见的Python函数
x = 2
print(abs(x))
x1 = 4
x2 = 2
print(max(x1, x2))
print(min(x1, x2))
print(pow(x1, x2))
print(round(3.5))
print(round(3.312, 2))
import math

x = 1.0
print(math.fabs(x))
print(math.ceil(x))
# 向上取整，不改变值
print(math.floor(x))
# 向下取整
print(math.exp(x))
# e^x
print(math.log(x))
# log_e x
print(math.sqrt(x))
# x^(1/2)
print(math.sin(x))
print(math.asin(x))
# arcsin(x)
print(math.cos(x))
print(math.acos(x))
# arccos(x)
print(math.tan(x))
print(math.degrees(x))
# 弧度转角度
print(math.radians(x))
# 角度转弧度
# 3.3 字符串和字符
ch = "A"
code = ord(ch)
# ASCII码
ch = chr(code)
# 对应字符
print("Hello World", end="")
# 不换行打印
string = str(12342)
# 数字转字符串
# 3.5 对象和方法
# python中所有的数据都是对象
n = 3
id(n)
type(n)
string.lower()
# 转小写
string.upper()
# 转大写
# 3.6 格式化数字和字符串
interest = 123.4342
print("the number is", format(interest, "10.2f"))
# 宽度为10，小数点后为2为的小鼠
print("the number is", format(interest, "10.2e"))
# 科学计数法
print("the number is", format(interest, "10.2%"))
# 百分数输出
print("the number is", format(interest, "<10.2f"))
# 默认为右对齐，加<改为左对齐
# d,x,o,b格式化十进制，十六进制，八进制，二进制整数
print(format("dfafiufhsiufhisufui", "10s"))
# 格式化宽度为20的字符串
# 3.7 绘制图形
# 3.8 绘制带颜色和字体的图形
