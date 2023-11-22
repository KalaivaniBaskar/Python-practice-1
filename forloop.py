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

