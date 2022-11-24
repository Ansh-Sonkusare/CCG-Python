CALORIES_PER_POUND = 3000
CALORIES_PER_MILES = 100

class Pet:
    __slots__=['species','name','weight','fur_color','age']

    def __init__(self,species,name,weight,fur_color,age=0):
        self.species=species
        self.name = name
        self.weight = weight
        self.fur_color= fur_color
        self.age = age

    def feed(self,calories):
        self.weight += calories / CALORIES_PER_POUND

    def walk(self,miles):
        self.weight -= miles * CALORIES_PER_MILES / CALORIES_PER_POUND

    # accessor:
    def get_name(self):
        return self.__name
    def get_weight(self):
        return self.__weight
        
# private classes:
class Pets:
    __slots__=['__species','__name','__weight','__fur_color','__age']

    def __init__(self,species,name,weight,fur_color,age=0):
        self.__species=species
        self.__name = name
        self.__weight = weight
        self.__fur_color= fur_color
        self.__age = age

    def feed(self,calories):
        self.__weight += calories / CALORIES_PER_POUND

    def walk(self,miles):
        self.__weight -= miles * CALORIES_PER_MILES / CALORIES_PER_POUND

    # accessor:
    def get_name(self):
        return self.__name
    def get_weight(self):
        return self.__weight