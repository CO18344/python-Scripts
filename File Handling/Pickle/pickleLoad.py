import pickle
fileHandler = open('Student.txt','rb')
while True:
    try:
        Obj = pickle.load(fileHandler)
        Obj.display()
    except EOFError:
        print('No more records  to read')
        break

