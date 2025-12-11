import time

class Pet:
    def __init__(self, name, hungry, thirsty, happy, age, tired, health):
        self.__name = name
        self.__hungry = hungry
        self.__thirsty = thirsty
        self.__happy = happy
        self.__age = age
        self.__tired = tired
        self.__health = health
    
    def show(self):
        print (f"{self.__name} is {self.__hungry}% hungry")
        print (f"{self.__name} is {self.__thirsty}% thirsty")
        print (f"{self.__name} is {self.__happy}% happy")
        print (f"{self.__name} is {self.__age} days old")
        print (f"{self.__name} is {self.__tired}% tired")
        print (f"{self.__name}'s heath is {self.__health}% ")

petname = input("Name your pet: ")
PET = Pet(f"{petname}","0","0","50","0","0","100")
die = 0
while die == 0:
    PET.show()