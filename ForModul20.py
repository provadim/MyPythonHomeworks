
class Student:
    def __init__(self,name,age,direction):
        self.name=name
        self.age=age
        self.direction=direction

    def ShowAboutStudent(self):
        print("Имя студента - ",self.name)
        print("Его возраст - ",self.age ,"а его направление обучения -", self.direction)
        
class Case:
    def __init__(self,name ,ForDirection,CountClasses):
        self.name=name
        self.ForDirection=ForDirection
        self.CountClasses=CountClasses
    