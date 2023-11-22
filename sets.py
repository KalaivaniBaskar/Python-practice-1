# Sets are unordered collection of unique ele. no duplicates 
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.


myset = set() # create set using constructor
myset.add("avvs")
print(myset) # {'avvs'} 

#False and 0, True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0, 1}

print(thisset) #{False, True, 'cherry', 'apple', 'banana'} 

#set methods 
# set.add('el')  adds elem
# set.remove('el') removes el from set 
# set.clear() clears the set, empties it 
# set.pop() The pop() method removes a random item from the set. 

set2 = set([1,2,3,1,2,3]) # set using a list ip
print(set2) #{1, 2, 3} 
print(set(list('Mississippi')))
# Boolean in Py are True and False (case sensitive)
print(1>4)
print(1>=1) 
a = None # initialize with None
print(type(a), a) #<class 'NoneType'> None