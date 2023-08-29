class Restaurant():

    def __init__(self,name,restype):
            self.name = name
            self.restype = restype
            self.served = 0

    def d_res(self):
        print("the restaurant's name is " + self.name.title()
            + ", and it's type is " + self.restype.title()
            + '\n')
            
    def o_res(self):
        print("the restaurant is now open\n")

    def set_num_servef(self,number):
         print("there are " + number + "people")

res1 = Restaurant('a','b')
print(res1.served)
num = input("how many people you have?\n")
res1.set_num_servef(num)

class Users():
    def __init__(self,f_n,l_n):
          self.f_n = f_n
          self.l_n = l_n
          self.login_attempts = 0
    
    def des(self):
        print("one of the users is " + self.f_n.title() 
               + " " + self.l_n.title())
     
    def gre(self):
        print("hellow " + self.f_n.title()
              + " " + self.l_n.title())
        
    def in_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user1 = Users('a','b')
nums = 0
while nums < 10:
    user1.in_login_attempts()
    print(user1.login_attempts)
    nums =nums + 1
user1.reset_login_attempts()
print(user1.login_attempts)