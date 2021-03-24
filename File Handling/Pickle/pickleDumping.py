import Selfpickle, pickle

Co18344 = Selfpickle.Student()
Co18339 = Selfpickle.Student()
Co18359 = Selfpickle.Student()

Co18344.updateAll(44,'Satvik',21)
Co18339.updateAll(39,'Mighty Raju',21)
Co18359.updateAll(59, 'Yaggu Don', 21)

Co18339.display()
Co18344.display()
Co18359.display()

with open('Student.txt','wb') as fileHandler:
    pickle.dump(Co18339,fileHandler)
    pickle.dump(Co18344,fileHandler)
    pickle.dump(Co18359,fileHandler)

