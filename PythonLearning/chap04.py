#4.2 布尔类型、数值和表达式
print(int(1<0))
print(bool(1<0))
#4.3 产生随机数字
import random
a=1
b=9
print(random.randint(a,b))#产生一个a,b间的随机整数,包括b
print(random.randrange(a,b))#同上,不包括
print(random.uniform(a,b))#产生一个a,b间的随机浮点数
#4.4 if语句
x = random.randint(a,b)
if x>(a+b)/2 :
    print(x)
#4.6 if-else语句
if x>(a+b)/2:
    print(x)
else:
    print((a+b)/2)
#4.7 嵌套if与多重if-else语句
#4.11 逻辑运算符