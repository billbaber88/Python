class Car(object):
    def __init__ (self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0

        

    def display_all(self):
        print "The price of this car is ", str(self.price)
        print "This car has a max speed of ", str(self.speed)
        print "The fuel level of this car is currently at ", str(self.fuel)
        print "The total number of miles driven on this car is ", str(self.mileage)
        if self.price > 10000:
            self.tax = 0.15
            print "The tax on this beaut is ", str(self.tax)
            return self
        else: 
            self.tax = 0.12
            print "The tax on this beaut is ", str(self.tax)
            return self
        

car1 = Car(5000, 75, "half full", 120000)
car1.display_all()
print "<-------------------->"
car2 = Car(7000000, 300, "empty", 500)
car2.display_all()
print "<-------------------->"
car3 = Car(200, 90, "full", 300000)
car3.display_all()
print "<-------------------->"
car4 = Car(30000, 120, "idk", 1200)
car4.display_all()
print "<-------------------->"
car5 = Car(50, 20, "full", 3000)
car5.display_all()
print "<-------------------->"
car6 = Car(10000, 70, "check yourself, you lazy bum", 90000)
car6.display_all()
print "<-------------------->"