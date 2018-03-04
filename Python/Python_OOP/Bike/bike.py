class Bike(object):
    def __init__(self, price, max):
        self.price = price
        self.max = max 
        self.miles = 0
    
    def displayinfo(self):
        print(self.price,self.max)
        return self
    
    def ride (self):
        self.miles = self.miles + 10
        print("Riding",self.miles)
        return self
    
    def reverse (self): 
        self.miles = self.miles - 5
        print("Reversing",self.miles)
        return self

bike1 = Bike(200,"25mph")
bike2 = Bike(300,"30mph")
bike3 = Bike(500,"50mph")

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()



    