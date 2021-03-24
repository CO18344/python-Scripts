class Student:
    def __init__(self):
        self.rollNumber = None
        self.name = None
        self.age = None
    
    def updateAll(self,rollNumber,name,age):
        self.rollNumber = rollNumber
        self.name = name
        self.age = age

    def display(self):
        print('Name = {:20s}, Roll Number = {:5d}, Age = {:5d}'.format(self.name, self.rollNumber, self.age))


if __name__ == '__main__':
    # Creating three objects
    Co18344 = Student()
    Co18344.updateAll(44,'Satvik',21)

    Co18339 = Student()
    Co18339.updateAll(39,'Mighty Raju',21)

    Co18359 = Student()
    Co18359.updateAll(59, 'Yaggu Don', 21)

    Co18339.display()
    Co18344.display()
    Co18359.display()
