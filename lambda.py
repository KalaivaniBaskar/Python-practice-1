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