# : and indendation are used to separate conditional statment and its code block 
myarray = [1,2,3,4,5,6,7,8]

for num in myarray:
    if num % 2 == 0:
        print(f'Even number: {num}')
    else :
        print(f'Odd number: {num}')