import random
string = input()
while string!="":
    a = random.randint(1,11)
    if a%3==1:
        print(string)
        break
    else:
        string = input()