import os, sys
if os.path.isfile('records.txt'):
    f = open('records.txt','r+b')
else:
    print('File Not Found')
    sys.exit()

Name = input('Enter the name to be updated in file: ')
Name = Name.encode()

NewName = input('Enter Updated name: ')
NewName = NewName.encode()

fileSize = os.path.getsize('records.txt')

recordSize = 20 # same records size was used in records.txt
NumOfRecords = int(fileSize/recordSize)

position = 0 # file pointer is at beginning

flag = False
for i in range(NumOfRecords):
    f.seek(position)
    recd = f.read(recordSize)

    if Name in recd:
        f.seek(-recordSize,1)
        f.write(NewName + ((recordSize - len(NewName)) * ' ').encode())
        flag = True
    position += recordSize
if flag:
    print('Updation process successful')
else:
    print("Record entered by you doesn't exist")
f.close()