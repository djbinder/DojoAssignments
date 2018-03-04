class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0
    
    def display_all(self):
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        print "Price: ", self.price
        print "Speed: ", self.speed
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage
        print "Tax: ", self.tax
        print('\n')

    
car1 = Car(500,"35mph","Full","15mpg")
car2 = Car(20000,"45mph","Empty","30mpg")
car3 = Car(100000,"900mph", "Super Full", "-20mpg")



car1.display_all()
car2.display_all()
car3.display_all()