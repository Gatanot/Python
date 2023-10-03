mark = 27
num = 0
low = 0 
high = 100
print("enter the number you guess")
num = input()
while num!=mark:
    if int(num) > mark:
        print("small")
    else:
        print("bigger")
    print("enter the number you guess")
    num = input()
print("right")