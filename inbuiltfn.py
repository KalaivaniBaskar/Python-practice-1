#inbuilt operators - range, enumerate, zip, in 

# range is an inbuilt op in Py , it generates a sequence of values based on the start, stop or step values we provied, 
# stop is mandatory and exclusive
#range(stop) -> range object 
#range(start, stop[, step]) -> range object

# Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).


# to get the generated values of a range fn , cast it to a list 
# range can be directly used in loop w/o casting
print(range(5))
print(list(range(5)))

for num in range(3,13,2):
    print(num)

# enumerate function : 
# it takes any iterable object and returns a list of tuples each containing index counter, and corresponding val 

word = 'abcde'
for item in enumerate(word):
    print(item)
for idx,val in enumerate(word):
    print(f'At index {idx}: {val}') 

#zip function: 

# this fn zips together multiple lists and pairs up the indexes 
# unpaired list items are left out 

list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd']
list3 = ['a1', 'b2', 'c3']

for item in zip(list1,list2, list3):
    print(item)

# to get op of the zip fn, cast it to a list
print(list(zip(list1,list2)))

# in operation 
print(1 in [1, 'a']) # True
print('a' in ['ab', 'a']) # True
print('a' in 'abc xyh') # True 
print('key1' in {'key1': 100})
print(100 in {'key1': 100}.values())  

# MATH FN - MIN MAX
mylist = [10, 20, 30, 50, 70]
print(min(mylist))
print(max(mylist))

#sum() takes an interable as i/p like a tuple or list
print(sum((1,2,3)))
print(sum([1,2,3])) 

