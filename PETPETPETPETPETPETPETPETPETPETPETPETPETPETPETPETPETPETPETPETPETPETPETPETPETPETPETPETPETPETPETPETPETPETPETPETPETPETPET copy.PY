import time

class Pet:
    def __init__(self, name, hungry, thirsty, happy, age, tired, health):
        self.__name = str(name)
        self.__hungry = int(hungry)
        self.__thirsty = int(thirsty)
        self.__happy = int(happy)
        self.__age = int(age)
        self.__tired = int(tired)
        self.__health = int(health)
    
    def show(self):
        print (f"{self.__name} is {self.__hungry}% hungry")
        print (f"{self.__name} is {self.__thirsty}% thirsty")
        print (f"{self.__name} is {self.__happy}% happy")
        print (f"{self.__name} is {self.__age} days old")
        print (f"{self.__name} is {self.__tired}% tired")
        print (f"{self.__name}'s heath is {self.__health}% ")
    def action(self, do):
        if do == "Play":
            self.__happy += int(25)
            print(f"{self.__name} is playing...")
        elif do == "Feed":
            self.__hungry = int(0)
            print(f"{self.__name} is eating...")
            time.sleep(5)
        elif do == "Sleep":
            self.__tired = int(0)
            print(f"{self.__name} is sleeping...")
            time.sleep(30)

petname = input("Name your pet: ")
PET = Pet(f"{petname}","50","0","50","0","0","100")
died = False
age = 0
while died == False:
    PET.show()
    do = input("What do pet? ")
    PET.action(do)
    PET = Pet(f"{petname}","67","0","50","0","0","100")