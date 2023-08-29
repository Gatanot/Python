class Restaurant():

    def __init__(self,name,restype):
            self.name = name
            self.restype = restype

    def d_res(self):
        print("the restaurant's name is " + self.name.title()
            + ", and it's type is " + self.restype.title()
            + '\n')
            
    def o_res(self):
        print("the restaurant is now open\n")

restaurant1 = Restaurant('a','b')
restaurant1.d_res()
restaurant1.o_res()

restaurant2 = Restaurant('b','c')
restaurant2.d_res()
restaurant2.o_res()

restaurant3 = Restaurant('c','d')
restaurant3.d_res()
restaurant3.o_res()

class Users():
    def __init__(self,f_n,l_n):
          self.f_n = f_n
          self.l_n = l_n
    
    def des(self):
        print("one of the users is " + self.f_n.title() 
               + " " + self.l_n.title())
     
    def gre(self):
        print("hellow " + self.f_n.title()
              + " " + self.l_n.title())
        
user1 = Users('a','b')

Users.des(user1)
Users.gre(user1)