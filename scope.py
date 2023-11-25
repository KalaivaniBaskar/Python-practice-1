# variable names stored in namespace
# scope determines the visibility of a var 
# LEGB rule : local, encl local, global, builtin
# local ie. within the fn , 
# enclosing fn locals ie. parent fn, 
# global - in the module, .py file, 
# built-in Py keywords - open, range , enumerate, list 

#GLOBAL
name = 'This is a global name'

def greet():
    # Enclosing function local
    name = 'Sammy'
    
    def hello():
        #local
        #name = "LOCAL"
        print('Hello '+name)
    
    hello()

greet() 
print(name)
# print(help(list)) 

x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)

# The global statement
# If you want to assign a value to a name defined at the top level of the program (i.e. not inside any kind of scope such as functions or classes), then you have to tell Python that the name is not local, but it is global. We do this using the global statement. It is impossible to assign a value to a variable defined outside a function without the global statement.

# to use a global var inside a fn and make changes to it use 'global' keyword inside fn on the var u need
# changes done on global var inside fn will reflect outside the fn too. 

x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)

# avoid global unless absolutely necessary,cuz not safe
print("below are global var")
print(globals())
print("below are local var")
print(locals())