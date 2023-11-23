# str.split() // splits by spaces 
# to split each char pass the string to a list constuctor
# el = list(mystr) 

name = "kalai"
occ = "engineer"
print(f'My name is {name}. I am an {occ}')
# field = input("What field are you working in? \n")
# print(f'I am working in the {field} field') 

print(name*3) 
print(list(name)) 
print(name.upper()) 
print(name.title()) 
print('She is a beautiful woman'.rpartition('is'))
print('She is a beautiful woman'.split())

s ='hello'
# Reverse the string using slicing
print(s[-1::-1])
print(s[::-1]) 

s ='hello'
# Print out the 'o'
# Method 1:
print(s[-1])
# Method 2:
print(s[len(s)-1]) 

# string 
def myfunc(word):
    res = ""
    for idx,val in enumerate(word):
        if idx % 2 == 0: 
            res = res + val.lower()
        else:
            res = res + val.upper()
    return res
print(myfunc('Anthropomorphism') )