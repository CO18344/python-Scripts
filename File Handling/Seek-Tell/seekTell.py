import sys, os
if os.path.isfile('seekTell.txt'):
    fileHandler = open('seekTell.txt','rb')
else:
    print('No such file found....')
    print('Terminating Application')
    sys.exit()

# initially file pointer is at the beginning so tell() will return 0
print(fileHandler.tell())

# Next calculating number of character in file.
fileHandler.seek(-1,2)  # setting file pointer to end of file
print(fileHandler.tell() + 1)

# Reading 398 from the file
fileHandler.seek(0)
while True:
    try:
        char = fileHandler.read(1)
        if char.decode() == '3':
            print(char.decode() + fileHandler.read(2).decode())
            break
    except EOFError:
        print('Not found 398')
        break

fileHandler.close()