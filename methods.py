# help(list.insert) # to get documentation
# help(list.pop) 

#def keyword 
# def fn_name() : 
# snake case for fn name = all lowercase w _ 
#  class names have camelcase 
# : indicates an upcoming indented block 
# docstring ? ''' multiline string to describe fn - optional 

def my_name(name): 
    print("your name: ",name)
my_name("kalai") 

def my_det(name, occ): 
    print("your name: ",name)
    print("your occ: ",occ)
my_det("kalai", "Engg") 

#return keyword to return value from the fn 
# it also ends the fn 

def add(a,b):
    return a+b
sum = add(5,9)
print(sum) 
print(type(sum) == "<class 'int'>")

def say():
    print("hi")
    print("hello")
    print("how are u")
say()
print(say) # not a fn call w/o () 

#if you dont pass arg it will throw a type err, so better have a default val
def my_name(name ='default user'): 
    print("your name: ",name)
my_name() 

# fn with return value 

#tuple unpacking w functions

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def get_max(work_hours):
    curr = 0
    emp = ""
    for empl, hrs in work_hours:
        if hrs > curr :
            curr = hrs
            emp = empl
        else:
            pass
    return (emp, curr) 
res = get_max(work_hours)
#can unpack the tuple result here
employee, maxhrs = get_max(work_hours)
print(res, employee) 

# employee, maxhrs, etc = get_max(work_hours)
# ValueError: not enough values to unpack (expected 3, got 2)