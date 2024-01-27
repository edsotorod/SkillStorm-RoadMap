'''
Topic - Classes and Objects

# define the state and behavior of an object
class Product:
    # instance variables
    price: float
    name: str
    is_active: bool
  
    # behavior
    def set_price(self, price):
        # data validation
        if price < 0:
        self.price = 0
        self.price = price
  
    def get_price(self):
        return self.price
    
    # constructor : initial values for the object (initialize)
    def __init__(self, name, price, is_active):
        self.name = name
        self.price = price
        self.is_active = is_active

# create an object using the class
tv = Product("TV", 500, True)
'''

# parent class
class Animal:
    weight: int
    name: str
        
    def speak(self):
        return "strange noise"

class Dog:
    breed: str
    
    def play(self):
        return "playing"
    
    # overriding / override
    def speak(self):
        return "Bark"
  
class Cat(Animal):
    def speak(self):
        return "Meow"


list = [Dog(), Cat(), Dog(), Animal()]
for animal in list:
    print(animal.speak())

'''
Topic - Classes and Objects
'''


'''
Topic - Classes and Objects
'''