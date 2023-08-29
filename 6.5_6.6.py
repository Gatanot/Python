rivrers = {'a':'a1',
           'b':'b1',
           'c':'c1',
           'd':'d1',
           'e':'e1',
           }

for key1,value1 in rivrers.items():
    print("The " + key1.title() + " runs through " + value1.title())

print('\n')

for key2 in rivrers.keys():
    print(key2)
    
print('\n')

for value2 in rivrers.values():
    print(value2)

print('\n')

names = {'a':'a1',
           'b':'b1',
           'c':'c1',
           'd':'d1',
           'e':'e1',
           }

lists = ['a','b','c','f','g']

for list in lists:
    if list.lower() in names.keys():
        print("thanks for report")
    elif list.lower() not in names.keys():
        print("please come to report")