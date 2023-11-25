class Dog:
    
    # Class Object Attribute, same for all instances of a class
    # so no need for 'self' 
    # purpose of self is to associate an instance with it's related attib 
    species = 'mammal'
    # when class attr is used in the methods of the class it can be referred with self or classname
    
    def __init__(self,breed,name):
        #below are instance level attributes, differs for each instance
        self.breed = breed
        self.name = name 

    # behaviour - methods 
    def bark(self):
        print(f"{self.name} says BOWOW!")

sam = Dog('Lab','Sam')
chica = Dog('Collie','Chica') 

print(sam.name, chica.name, sam.species, chica.species)
sam.bark()
chica.bark() 

class Circle:
    pi = 3.14
    # when class obj attrib is used in the methods of the class it can be referred with self or classname

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi
        
    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
c.setRadius(20)
print('Area is: ',c.area)
print(f'Circumference: {c.getCircumference():.2f}')