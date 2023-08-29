name1 = {
    'first_name':'a1',
    'last_name':'a2',
    'age':1,
    'city':'a3',
    }

name2 = {
    'first_name':'b1',
    'last_name':'b2',
    'age':2,
    'city':'b3',
    }

name3 = {
    'first_name':'c1',
    'last_name':'c2',
    'age':3,
    'city':'c3',
    }

persons = [name1,name2,name3]
for person in persons:
    print(person)
    print('\n')

print('\n')

pet1 = {'name':'a1',
        'owner':'a2',
        }
pet2 = {'name':'b1',
        'owner':'b2',
        }
pet3 = {'name':'c1',
        'owner':'c2',
        }
pets = [pet1,pet2,pet3]

for pet in pets:
    print("it's name is " + pet['name'] + ", and it's onwer is " + pet['owner'] +'\n')

print('\n')

fp = {'a':['a1','a2','a3'],
      'b':['b1','b2','b3'],
      'c':['c1','c2','c3'],
      }
for key,Value in fp.items():
    print(key + " is a friend of mine. he like ")
    for value in Value:
        print(value)

print('\n')

num = {'a':[1,2,3],
       'b':[1,2,3],
       'c':[1,2,3],
       'd':[1,2,3],
       'e':[1,2,3],
       }
for key1,key2 in num.items():
    print(key1 + " like number " + str(key2) + " most")

print('\n')

citys = {'a':{'country':'a1','population':'a2','fact':'a3'},
         'b':{'country':'b1','population':'b2','fact':'b3'},
         'c':{'country':'c1','population':'c2','fact':'c3'},
         }
for city,infor in citys.items():
    print(city + " is a city." + 
          " it belong to country " + infor['country'] + 
          ". it's population is " + infor['population'] + 
          ". a fact of it is " + infor['fact']
          )
