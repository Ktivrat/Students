import random

# ⦁	Необходимо реализовать для класса Student атрибут id, который должен присваиваться случайным образом
# ⦁	Сделать сортировку списка students по убыванию атрибута id (от 100 до 1 к примеру)


class Student:
    def __init__(self, name='', group='', gpa=0):
        self.__name = name
        self.__group = group
        self.__gpa = gpa
        self.__id = random.randint(1, 100)
    
    def show(self):
        print(f"ID: {self.__id}, Name: {self.__name}, Group: {self.__group}, GPA: {self.__gpa}")
    
    @property
    def getgroup(self):
        return self.__group
    
    @property
    def getgpa(self):
        return self.__gpa
    
    @property
    def getid(self):
        return self.__id
