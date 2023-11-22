myfile = open('./testfile.txt') 
#"r" for read, and "t" for text are the default values, you do not need to specify them.
# modes r 
print(myfile) 
#<_io.TextIOWrapper name='./testfile.txt' mode='r' encoding='cp1252'>
print('first read:')
print(myfile.read())
# during 1st read 
# This is a text file sample
# this is the 2nd line in file
# this is the 3rd line in file
print('read w/o seek:')
print(myfile.read())

#during 2nd read, the cursor is at end of file so o/p is blank
#to reset the cursor to beginning 
myfile.seek(0)
print("read after seek:")
print(myfile.read()) 
myfile.seek(0)
# to read file line by line 
print("read line by line:")
print(myfile.readline()) #line 1
print(myfile.readline()) #2
print(myfile.readline()) #3
print(myfile.readline()) #empty
print(myfile.readline()) #empty
myfile.seek(0) 

#get the  the file by lines in a list
print(myfile.readlines())
#['This is a text file sample \n', 'this is the 2nd line in file \n', 'this is the 3rd line in file']

#file methods basic
# open()
# read() 
# readlines()
# seek() 
# readline() 
myfile.close()  # close file otherwise it remains open 
#opening a file outside pwd 
# "C:\Users\Kalai\Desktop\testfile2.txt" 
# \ is escape char so use it twice \\Users in windows
# for linux /  
myfile2 = open("C:\\Users\\Kalai\\Desktop\\testfile2.txt" ) 
print(myfile2)
print('second file read:')
print(myfile2.read())
myfile2.close()  
print("open file: 'with' keyword")
# to not worry about closing files 
with open('./testfile3.txt') as myfile3:
    file_content = myfile3.read()
print(file_content) 

