class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Rat(Animal):
  pass
# this was Rat inherits everything from Animal
# has no attrib of its own
r = Rat() #Animal created

#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# to call parent's init use Parentclass.init or super() for empty init , super().init()other param?

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        self.name=name
        print("Dog created", self.name)

    def whoAmI(self):
        print("Dog ", self.name)

    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def __init__(self,name):
        # Animal.__init__(self)
        #super()
        self.name=name
        print("Cat created", self.name)

    def whoAmI(self):
        print("Cat")

    def bark(self):
        print(f"{self.name} says Meow!")

d = Dog(name="Scooby")
c = Cat(name="Ash") 
fido = Dog('Fido')
iris = Cat('Iris')
# diff objects can share the same method name - polymorphism 

for pet in [d,c,fido,iris]:
    print(type(pet))
    pet.bark() 

# Abstract classes : these are classes that are never instantiated but only serve as base class. 
# it has constructor __init__ 
# it has 
