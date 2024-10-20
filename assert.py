class Item:
    pay_rate=0.8 # The pay rate after 20% discount
    def __init__(self,name:str, price:float,quantity:float):
       
       #Run validations to the received
       assert price >=0 , "price {price} is not greater than or equal zero!"
       assert quantity >=0,"price {quantity} is not greater than or equal zero!"
        #Assign to self object
       self.name=name 
       self.price= price 
       self.quantity= quantity 
    

    def calculate_total_price(self):
        return  self.price * self.quantity
    def apply_discount (self): 
        self.price= self.price* Item.pay_rate

item1= Item("Phone",100,5)
item2 = Item("Laptop",1000,1)
item1.apply_discount()
print(item1.price)
