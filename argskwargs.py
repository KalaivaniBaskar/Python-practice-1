# Arbitrary Arguments and keyword args
# *args = args is a tuple that receives all positional arguments passed during fn call

def my_function(*kids):
  print(kids)
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# **kargs keyword arguments creates a dictionary and stores the variable and value
# *args = tuple, **kwargs = dict
def myfunc(**kwargs):
  print(kwargs)
  if 'fruit' in kwargs:
    print(f'the fruit is {kwargs['fruit']}')
# fruit = "apple"
# myfunc(fruit) this way wnt work w kwargs
myfunc(fruit="orange") 

#using both *args and **kwargs
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass
        
myfunc('eggs','spam',fruit='cherries',juice='orange') 

# always *args first and then **kwargs