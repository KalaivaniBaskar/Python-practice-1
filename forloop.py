# : and indendation are used to separate conditional statment and its code block 
myarray = [1,2,3,4,5,6,7,8]

for num in myarray:
    if num % 2 == 0:
        print(f'Even number: {num}')
    else :
        print(f'Odd number: {num}') 

array_sum = 0 
for num in myarray:
    array_sum = array_sum + num
print(array_sum) 

# be careful with indentation 
# lines with same indentation = same code block
array_sum = 0 
for num in myarray:
    array_sum = array_sum + num
    print(array_sum) 

# iterating strings 
word = "Python Rules"
for char in word:
    print(char) 

#iterating Tuples
mytuple = ('assd', 'fdf', 'rere', 'oioio')
for item in mytuple:
    print(item)

#tuple unpacking is similar to array destructuring in JS 
mytuplist = [(1,2), ("name","xyz"), ("k", 89)]
for (a,b) in mytuplist:
    print(f'item1 is {a}, item2 is {b}')

bill = [("veg", 10, 320), ("fruit", 4, 450), ("util", 12, 890)]
for (name, qty, price) in bill:
    print(f'Category: {name}, No. items: {qty}, Price: {price}') 

#iterating Dictionaries 
d = {'k1':1,'k2':2,'k3':3} 
# this iterates through the keys in the dict, can use key to access val
for item in d:
    print(item, d[item]) 

# this iterates through only the values in the dict
for val in d.values():
    print(val)

# another method is use items() method of dict and get key&value as tuples in a list 
for (key,val) in d.items():
    print(f'Key: {key}, Value : {val}')  


# LIST COMPREHENSION: 
#List comprehensions allow us to build out lists using a different notation. You can think of it as essentially a one line for loop built inside of brackets. For a simple example: 

# a flattened out for loop - el for el in iterable-obj
alist = [ c for c in 'kalaivani']
print(alist) 

numlist = [ num for num in range(0,6)]
print(numlist) 

# can perform op on each el
numlist = [ num**2 for num in range(0,6)]
print(numlist)  

# we can also apply condition and filter out el 
numlist = [ num**2 for num in range(0,6) if num%2==0]
print(numlist) 

#perform common op on all el of a list
cel = [0, 10, 20, 34.5]
far = [ ( (9/5)*temp + 32) for temp in cel]
print(far)

# using if and else can get tricky 
numlist = [ num**2 if num%2==0 else num**3 for num in range(0,6) ]
print(numlist) 

nestlist = [ x*y for x in [2,4,6] for y in [10,100,1000]]
print(nestlist)