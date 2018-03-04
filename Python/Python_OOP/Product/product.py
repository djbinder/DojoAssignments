class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.return_reason = ""

    def sell(self):
        self.status = "sold"
        return self

    def addtax(self, tax):
        self.price = (self.price * tax) + self.price
        return self
    
    def return_product(self, condition):
        self.return_reason = condition
        if condition is "defective":
            self.status = "defective"
            self.price = 0
        if condition is "returned in box":
            self.status = "for sale"
        if condition is "box opened":
            self.status = "used"
            self.price = self.price * .8
        return self

    def display_info(self):
        if self.status is "defective":
            print "Price: ", self.price
            print "Item Name: ", self.item_name
            print "Weight: ", self.weight
            print "Brand: ", self.brand
            print "Status: ", self.status
            print "Return Reason: ", self.return_reason
        if self.status is "used":
            print "Price: ", self.price * .8
            print "Item Name: ", self.item_name
            print "Weight: ", self.weight
            print "Brand: ", self.brand
            print "Status: ", self.status
            print "Return Reason: ", self.return_reason
        else:
            print "Price: ", self.price
            print "Item Name: ", self.item_name
            print "Weight: ", self.weight
            print "Brand: ", self.brand
            print "Status: ", self.status

prod1 = Product(20000,"shoes","10lbs","Nike")
prod2 = Product(10,"boots","1111lbs","boots brand")

prod1.return_product("box opened").display_info()
print ("\n")
prod2.display_info()



# print prod1.brand
# print ("\n")

# prod1.addtax(.15).display_info()
# print ("\n")

# prod1.sell().display_info()
# print ("\n")

