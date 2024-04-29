# 6.2 定义一个函数
# 6.3调用一个函数
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(max(23, 132))


# 6.4带或不带返回值的函数
# 6.5位置参数与关键字参数
def nprint(message, n=1):
    for i in range(n):
        print(message)


nprint("sdafsa", 3)
nprint("dasas")
# 位置参数不能出现在关键字参数之后
#6.6通过传递引用来传递参数
#调用函数时，实参的值就被传递给形参，这个值通常就是对象的引用值
#如果实参是一个数字或一个字符串，不管函数中的形参有没有变化，实参是不受影响的
#6.7模块化代码
#6.9变量的作用域
#6.10 默认参数
#6.11返回多个值
#6.13函数抽象和逐步求精