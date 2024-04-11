t=['a','b','c']
message1="i invited "+t[0]+","+t[1]+","+t[2]+" to the party"
print(message1)
print(t[0]+" is not free")
t[0]='d'
message2="i invited "+t[0]+","+t[1]+","+t[2]+" to the party"
print(message2)
print("i found a bigger table")
t.insert(0,'f')
t.insert(1,'g')
t.append('h')
message3="i invited "+t[0]+","+t[1]+","+t[2]+","+t[3]+","+t[4]+","+t[5]+" to the party"
print(message3)
print("i can invite only 2 peole now")
message4=t.pop()
print(message4+" is not allowed to be")
message4=t.pop()
print(message4+" is not allowed to be")
message4=t.pop()
print(message4+" is not allowed to be")
message4=t.pop()
print(message4+" is not allowed to be")
print(t[0]+","+t[1]+" is here")
del t[1]
del t[0]
print('\n')
print(t)