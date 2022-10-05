
from asyncio import proactor_events


class Student:
    def __init__(self,name,age,direction, yearOfDiplom):
        self.__name=name
        self.__age=age
        if (len(direction)==0):
            print(self.__name,"- вообще не является студентом, так как у него отсутствует направление")
            self.__direction="Пока не студент"
        else:
            self.__direction=direction
        if (yearOfDiplom<2022):
            print(self.__name," -не является студентом так как уже закончил ВУЗ в ",yearOfDiplom," году")
            self.__yearOfDiplom="Уже не студент"
        else:
            self.__yearOfDiplom=yearOfDiplom
    def set__name(self,name):
        self.__name=name
    #@property
    def get__name(self):
        return self.__name
    def get__direction(self):
        return self.__direction
   






    def ShowAboutStudent(self):
        print("Имя студента - ",self.__name)
        print("Его возраст - ",self.__age )
        print("а его направление обучения -", self.__direction)
        print("Диплом  был/будет от ",self.__yearOfDiplom,"-го года\n")
class Case:
    def __init__(self,name ,ForDirection,CountClasses):
        self.name=name
        self.ForDirection=ForDirection
        self.CountClasses=CountClasses

#FirstStudent=Student("Вадим",52,"Data Scientist",2022)
#SecondStudent=Student("Вася","Неопределен","","")
#print(FirstStudent.direction)
#FirstStudent.ShowAboutStudent()
#SecondStudent.ShowAboutStudent()