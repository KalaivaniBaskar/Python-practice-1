import one

print("top lvel in two.py")

one.func()

if __name__ == "__main__"  : 
    print("two.py is run directly") # py pgm run directly at cmd line
else:
    print("two.py has been imported") 

#when this file is run, op is:

# hello
# top level one.py
# one.py has been imported
# top lvel in two.py
# func in one.py
# two.py is run directly