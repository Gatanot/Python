def make_shirt(size,words):
    print("the size of shirt is " + size +
          ", and the words on it is " + words)
    
size = input("the size you want: \n")
word = input("the word you want: \n")

make_shirt(size,word)

print('\n')

def make_shirt2(size = 'L',words = 'i love Python'):
    print("the size of shirt is " + size +
          ", and the words on it is " + words)

a = 0
print("if you don't decied yet ,type no please")
while a < 3:
    size1 = input("the size you want: \n")
    word2 = input("the word you want: \n")
    if size1.lower() == 'no' and word2.lower() == 'no':
        make_shirt2()
    elif size1.lower() == 'no' and word2.lower() !='no':
        make_shirt2(words=word2)
    elif size1.lower() != 'no' and word2.lower() == 'no':
        make_shirt2(size=size1)
    else:
        make_shirt2(size=size1,words=word2)
    a = a + 1

print('\n')

def describe_city(name,country = 'a'):
    print(name + " is in " + country)
b=0
while b < 3:
    name1 = input("a city's name please")
    country1 = input("it's country please")
    if country1:
        describe_city(name = name1,country = country1)
    else:
        describe_city(name = name1)
    b = b+1