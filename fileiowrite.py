# mode = r - read , w - write / overwrite or create new ,
# a - append - add to existing content of file
# r+ read n write , w+ - write n read - overwrite / new

#appending TO FILE : 
with open('./testfile.txt', mode = 'r') as myfile:
    myfile_cotent = myfile.read()
    print(myfile_cotent)

with open('./testfile.txt', mode = 'a') as f:
    f.write('\nappending 4th line in file')

with open('./testfile.txt', mode = 'r') as myfile:
    myfile_cotent = myfile.read()
    print(myfile_cotent)

#writing a file - create / overwrites
with open('newfile1.txt', mode='w') as f:
    f.write('this new file is created')
with open('newfile1.txt', mode='r') as f:
    print(f.read())