import os, sys

if os.path.isfile('records.txt'):
    f = open('records.txt','rb')
else:
    print('File Not Found')
    sys.exit()

Name = input('Enter the name to be deleted in file: ')
Name = Name.encode()

# creating new file
f2 = open('temp.txt','wb')

fileSize = os.path.getsize('records.txt')

recordSize = 20 # same records size was used in records.txt
NumOfRecords = int(fileSize/recordSize)

position = 0 # file pointer is at beginning

for i in range(NumOfRecords):
    f.seek(position)
    recd = f.read(recordSize)

    if Name not in recd:
        f2.write(recd)
    position += recordSize


f.close()
f2.close()

os.remove('records.txt')
os.rename('temp.txt','records.txt')