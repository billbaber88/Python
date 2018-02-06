class Product(object):
    def __init__ (self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = 0

    def sale(self):
        self.status = "sold"
        return self

    def tax(self):
        self.price = self.price * 1.08
        return self
    
    def returnProduct(self, reason, open):
        if reason is "defective":
            self.status = "broken"
            self.price = 0
            return self
        elif open is "yes":
            self.status = "used"
            self.price = self.price*.80
            return self
        else:
            self.status = "for sale"
            return self
    
    def display_info(self):
        print "the product is", str(self.name)
        print "the brand is", str(self.brand)
        print "this product is", str(self.status)
        print "the price is $", str(self.price)

grapes = Product(2, "grapes", 1, "jewel")
grapes.sale().tax().returnProduct("defective", "yes").display_info()
print '<------->'
baseball_glove = Product(30, "Mitt", 2, "Rawlings")
baseball_glove.sale().tax().display_info()
print '<--------------->'
baseball_glove.sale().tax().returnProduct('no', "yes").display_info()
        
        
