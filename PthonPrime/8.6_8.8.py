def city_country(city,country):
    message = city + "," + country
    return message

while True:
    print("enter no to quit")
    city1 = input("a city please:\n")
    if city1 == 'no':
        break
    country1 = input("it's country please:\n")
    if country1 == 'no':
        break
    print(city_country(city1,country1))

def make_album(singer,name):
    album = {'singer':singer,
             'name':name,
             }
    return album
while True:
    print("enter no to quit")
    singer1 = input("a singer please:\n")
    if singer1 == 'no':
        break
    name1 = input("it's album's please:\n")
    if name1 == 'no':
        break
    print(make_album(singer1,name1))