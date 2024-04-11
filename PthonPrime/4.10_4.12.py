AS=[1,2,3,4,5,6,7]
print("the first three items in the list are:")
for A in AS[:3]:
    print(A)
print("the three items in the list are:")
for A in AS[2:5]:
    print(A)
print("the last three items in the list are:")
for A in AS[-3:]:
    print(A)

Pizzas=['a','b','c','d']
a_Pizzsas=Pizzas[:]
Pizzas.append('e')
a_Pizzsas.append('f')
print("my favorite pizzas are:")
for Pizzsa in Pizzas:
    print(Pizzsa)
print("my friend's favorite pizzas are:")
for a_Pizzsa in a_Pizzsas:
    print(a_Pizzsa)