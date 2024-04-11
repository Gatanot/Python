message = input("type the food you want,if you want to qiut, type quit: \n")
while message != 'quit' :
    print("i will add " + message +" into your pizza\n")
    message = input("type the food you want,if you want to qiut, type quit: \n")

print('\n')

age = input("type your age: \n ")
ded = True
while ded == True:
    if int(age) <= 0:
        ded = False
    elif int(age) < 3:
        print("free")
    elif int(age) < 12:
        print("10 dollars")
    elif int(age) >= 12:
        print("15 dollars")
    age = input("type your age: \n ")

