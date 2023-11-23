from random import shuffle, randint

mylist = [1,2,3,4,5,6,7,8,9]
print(mylist)
shuffle(mylist)
print(mylist) 

# shuffle does not return val, alters og list

#randint between a given range, both inclusive
print(randint(1,100)) 

#input fn - get input from user. 
# by def, all inputs are received as string

# res = int(input('Enter a number: \n'))
# print(f'you entered {res}') 

mylist = [1,2,3,4,5,6,7,8,9]
print(mylist) 

def my_shuffle(lst):
    shuffle(lst)
    return lst

#does not alter mylist
print(my_shuffle([x for x in mylist]), mylist)
# alters mylist
print(my_shuffle(mylist), mylist) 

mylist = [' ','O',' ']
def my_shuffle(lst):
    shuffle(lst)
    return lst

def guess_pl():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2:  ")
    return int(guess)

def check(shuff, guess):
    if(shuff[guess] == 'O'):
        print('Correct !')
    else:
        print("Oops wrong!", shuff)

# execute
shuffled_lst = my_shuffle(mylist) 
guess = guess_pl()
check(shuffled_lst,guess)

