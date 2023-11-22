print(1 == '1') #False
print(1 == 1) #True
#No implicit conversions in Py 

#BODMAS rule
# 4 * (6+5)  44
# 4 * 6 + 5  29
# 4 + 6 * 5  34

print(100/10*10-10+10.25) # 100.25
print(type(3 + 1.5 + 4)) #float 

# Answer before running cell
3.0 == 3 #True
print(3.1 == 3) #False
# Answer before running cell
4**0.5 != 2 #False , 2.0 == 2 true 

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1'] #false 

# Square root:
4**0.5 # 2.0 , always float 

# == is case sensitive and type sensitive 
# != checks for  'not equal'
#logical op: and , or, not 
not(1 == 1) # false 

# 2 < 3 > 10 is nothing but 2<3 and 3>10