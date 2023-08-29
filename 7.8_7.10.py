sandwich_orders = ['a','b','c']
finished_sandwiches = []
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(" i made your " + sandwich + " sandwich")
print("all sandwichs have been made, like:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

print('\n')

print("all a sandwich are sold out")
while 'a' in sandwich_orders:
    sandwich_orders.remove('a')
while 'a' not in sandwich_orders:
    print("threr is really no a")
    break

print('\n')

lists = []
ded = True
while ded == True:
    place = input("if you could visit one place, "
        "where would you go?")
    lists.append(place)
    message = input("any one more place?").lower()
    if message == 'no':
        ded = False
print(lists)