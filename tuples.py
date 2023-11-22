# tuples are similar to list but tuples are immutable 
# so you cannot just change a part of it 
# tuples use () , list use []
# once an el is inside tuple it cannot be reassigned
# i.e. when an el is assigned an index , it cannot be grabbed and reassigned like we do in list 

# my_tup = (1,2,3)
# my_list = [1,2,3] 

# tuple can also store mixed data in it ( "abc", 1.454, 90)

#methods  - has very few methods since it is immutable 
# no append or pop etc 
# len(tupname) for length
# using slicing done on string and lists work here too
# tupnew = (1,2,4,'d','j')
# len(tupnew) 5
# tupnew[1:] (2, 4, 'd', 'j')
# tupnew[1::2] (2, 'd') 

# count(), index()
# # tupnew = (1,2,4,'d','j', 'd', 'c')
# tupnew.count('d') 2 # no of occurence 
# tupnew.index('d') 3 # first occurence index of an el 

# tuple is immutable - does not allow item assignment
# tupnew[1] = "two"
# TypeError: 'tuple' object does not support item assignment