# map applies a given fn on each item of an given iterable
# (__func: (_T1@__new__) -> _S@map, __iter1: Iterable[_T1@__new__], /) -> map[_S@map]
# map(func, *iterables) --> map object

# Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.

def square(num):
    return num**2

mylst = [1,2,3,4,5]
print(map(square, mylst))
print(list(map(square, mylst))) 

def even_odd(word):
    if len(word) % 2 == 0:
        return word.upper()
    else:
        return word.lower()

s = "This is a even odd sentence notice what map does" 
lst = s.split()
print(list(map(even_odd, lst))) 

#filter fn the element that gives condition True is retained, those that give False are left out
# (__function: None, __iterable: Iterable[_T@filter | None], /) -> filter[_T@filter]
# filter(function or None, iterable) --> filter object

# Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.
mylst = [1,2,3,4,5,6]
def check_e(num):
    return num%2 == 0 #return boolean 
print(filter(check_e, mylst))
print(list(filter(check_e, mylst))) 


#simplifying a regular fn into Lambda expressions
# lambda expression is also known as anonymous fn
def square(n):
    return n**2
def square(n): return n**2 
square = lambda n: n**2
print(square(4)) 

# we don't usually name lamda fn and use it, 
# commonly lambda fn are used w map and filter

mylst = [1,2,3,4,5,6]
print(list(map(lambda n: n**2,mylst)))
print(list(filter(lambda n: n%2==0,mylst)))

#grab 1st letters of each word
mynames = ['kalai', 'usha', 'saba', 'aji', 'kavi', 'bas']
print(list(map(lambda n: n[0], mynames)))
print(list(map(lambda n: n[::-1], mynames)))