alien_coloe=['green']
if 'green' in alien_coloe:
    print("you got 5 point")
else:
    print('you got 0 poiny')

print('\n')

if 'green' in alien_coloe:
    print('you got 5 point')
else:
    print('you got 0 point')

print('\n')

if 'green' in alien_coloe:
    print('you got 5 point')
elif 'yellow' in alien_coloe:
    print('you got 10 point')
else:
    print('you got q5 point')

print('\n')

age = 23
if (age < 2):
    print('婴儿')
elif (age < 4):
    print('学步')
elif (age < 13):
    print('儿童')
elif (age < 20):
    print('少年')
elif (age < 65):
    print('成人')
elif (age > 65 and age == 65):
    print('老人')

print('\n')

fruits = ['a','b','c']
a_fruits = ['a','b','c','d','e']
for a_fruit in a_fruits:
    if a_fruit in fruits:
        print("you really like "+a_fruit)