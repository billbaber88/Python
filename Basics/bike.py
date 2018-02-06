class Bike(object):
    def __init__ (self, price, max_speed):
        self.price = price
        self.speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "The cost of this bike is $" + str(self.price)
        print "The max speed of this bike is " + str(self.speed) + "mph."
        print "The total miles traveled on this bike so far is " + str(self.miles)

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "beep beep beep beep"
        self.miles -= 5
        return self

bike1 = Bike(100, 20)
bike1.ride().ride().ride().displayinfo()

bike2 = Bike(5, 5)
bike2.ride().ride().reverse().reverse().displayinfo()

bike3 = Bike(1000, 5)
bike3.reverse().reverse().reverse().displayinfo()