num = 11 
while num > 0:
    print(num)
    num = int(num / 2)
else : 
    print("exit:", num) 

# else block in while is optional 
# it is executed only once when condi is false

# break : breaks out of current loop 
num = 0 
while num >= 0 :
    print(num)
    num = num+ 1 
    if num > 5:
        break

# continue :  goes to the next iteration, skips the code below it
name = "kalai"
for c in name:
    if c == 'a': 
        continue
        print(c)
    else : 
        print(c)

# pass : does nothing
arr = [1,2,3]
for i in arr: 
    # must contain some code here else error
    # in such cases if you have no code to execute use pass
    pass

