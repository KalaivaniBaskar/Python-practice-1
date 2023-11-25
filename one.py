# all lines of code at indentation 0 are run when this file is called
print("hello")

# built in variable  __name__
# __name__ is assigned a valued depending on how this file is run 

#if this py file is run directly, assign
# __name__ = "__main__"  

def func():
    print("func in one.py")

print("top level one.py")

if __name__ == "__main__"  : 
    print("one.py is run directly") # py pgm run directly at cmd line
else:
    print("one.py has been imported") 
# when this file is run directly op is
# hello
# top level one.py
# one.py is run directly