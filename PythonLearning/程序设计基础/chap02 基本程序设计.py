import time

currenttime = time.time()
# 获取当前时间
print(currenttime)
totalseconds = int(currenttime)
currentseconds = totalseconds % 60
totalminutes = totalseconds // 60  # 得到整数的除法
currentminutes = totalminutes % 60
totalhours = totalminutes // 60
currenthours = totalhours % 24
print("current time is: ", currenthours, ":", currentminutes, ":", currentseconds)
