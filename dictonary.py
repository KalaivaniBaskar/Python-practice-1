# dictionaries are like object datatype in JS 
# { key : value }

# Dictionaries FAQ

# 1. Do dictionaries keep an order? How do I print the values of the dictionary in order?

# Dictionaries are mappings and do not retain order! If you do want the capabilities of a dictionary but you would like ordering as well, check out the ordereddict object lecture later on in the course! 

# the key value pairs in dict do not maintain a specific order or sequence 

#  d={'k1':[1,2,3]}

# What is the output of d['k1'][1] ans: 2 

# Dictionaries are mutable. You can edit a key in dict and change its value. 
# just like how lists are mutable, we can change value at a specific index 

#d.keys() // gives list of keys of a dict
# d.values() // gives list of values 

# Method to return tuples of all items  (we'll learn about tuples soon)
# d.items() // ([('key1', 1), ('key2', 2), ('key3', 3)])

# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
# Grab 'hello'
# d['simple_key'] 

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
# d['k1']['k2']  

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# d['k1'][0]['nest_key'][1][0]
#Grab hello


# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]} 
# d['k1'][2]['k2'][1]['tough'][2][0]

