user_names = ['admin','a','b','c','d']
if user_names :
    for user_name in user_names:
        if user_name == 'admin':
            print('hello, would you like to see a status report?')
        else:
            print("hello, " + user_name + "thank you for use")
else:
    print("no users")

print('\n')

current_users = ['a','b','c','d','e']
new_users = ['A','b','f','g','h']
for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print(new_user +' has been used')

print('\n')

list = [1,2,3,4,5,6,7,8,9]
for num in list:
    if num == 1:
        print(str(num) + "st")
    elif num ==2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")