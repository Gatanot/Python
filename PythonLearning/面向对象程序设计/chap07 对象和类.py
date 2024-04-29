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
