# lists are like array 
# list = [ ]
# len(listname) gives length 
# list.append('newel') adds el to the end of list 
# list.pop() removes last el from list 
# list.pop(idx) removes el at specified idx 
# list.sort() - sorts the list elements 
# sort() - alters og list, no return value 'None' datatype
# bultin fn sorted() - returns sorted list, retains og list
# list.reverse() - reverses the list el 
# list are mutable, unlike strings 
# list[idx] value can be changed 
# concat 2 list or more list with + 
# We can also use + to concatenate lists, just like we did for strings.

# my_list + ['new item']
# ['one', 'two', 'three', 4, 5, 'new item'] 

a = [3,1,2].sort()
print(a) # sort fn returns None, it only alters og list 
a = [3,1,2]
a.sort()
print(a)

# Method 2:
mylist = []
mylist.append(0)
mylist.append(0)
mylist.append(0)
print(mylist)

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4) 

print([0]*3)
print(['a']*5)

newlist = [ 9,3,6,2,7]
print(sorted(newlist), newlist)
