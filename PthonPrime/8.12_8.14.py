def print_sandwich(*foods):
    print("this sandwich nedds the following foos:\n")
    for food in foods:
        print(food)
        print('\n')

a = 0
b = ['a']
while a < 3:
    b.append(str(a))
    print_sandwich(b)
    a = a + 1

