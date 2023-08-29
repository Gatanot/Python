class Car():
    # 一次模拟汽车的尝试
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("whis car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reding:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")

    def inc_odometer(self,miles):
        self.odometer_reading += miles

class ECar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def des_battery(self):
        print("this car has a " + str(self.battery_size) + " -KWh battery.")

my_car = ECar('tesla','modles','2016')
print(my_car.get_name())
my_car.des_battery()