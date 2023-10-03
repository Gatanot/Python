car = input("waht kind of car do you want: \n ")
print("let me see if there is a " + car)

print('\n')

num = input("how many people do you have? \n")
if int(num) > 8:
    print("no free table")
else:
    print("therr is free table")

print('\n')

num1 = input("press any number you like: \n")
if int(num) % 10 == 0:
    print("it is an integer multiple of 10")
else:
    print("it is not an integer multiple of 10")
