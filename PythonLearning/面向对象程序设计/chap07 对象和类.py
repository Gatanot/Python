# 7.2为对象定义类
import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius**2 * math.pi

    def setRadius(self, radius):
        self.radius = radius


c1 = Circle(5)
c2 = Circle()
print(c1.getPerimeter())
print(c1.getArea())
print(c2.getPerimeter())
print(c2.getArea())
c2.setRadius(6)
print(c2.getPerimeter())
print(c2.getArea())
# 7.3UML类图
# 7.4不变对象和可变对象
# 7.5隐藏数据域
# 在属性名前加__将其定义为私有
# 7.6类的抽象和封装
# 7.7面向对象的思考
