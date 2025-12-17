import time

class Pet:
    def __init__(self, name, hungry, happy, age, tired,):
        self.__name = str(name)
        self.__hungry = int(hungry)
        self.__happy = int(happy)
        self.__age = int(age)
        self.__tired = int(tired)
    
    def show(self):
        print(" ")
        print (f"{self.__name} is {self.__hungry}% hungry")
        print (f"{self.__name} is {self.__happy}% happy")
        print (f"{self.__name} is {self.__tired}% tired")
        print (f"{self.__name} is {self.__age} days old")
    def action(self, do):
        if do == "Play":
            self.__happy += 50
            self.__age += 0.1
            print(f"{self.__name} is playing...")
            time.sleep(5)
        elif do == "Feed":
            self.__hungry -= 50
            self.__age += 0.1
            print(f"{self.__name} is eating...")
            time.sleep(5)
        elif do == "Sleep":
            self.__tired = -15
            self.__age += 0.2
            print(f"{self.__name} is sleeping...")
            time.sleep(10)
    def subtract(self):
        self.__happy -= 10
        self.__hungry +=10
        self.__tired += 15

petname = input("Name your pet: ")
PET = Pet(f"{petname}","50","50","0","0")
died = False
age = 0
while died == False:
    PET.show()
    do = input("What to do pet? ")
    PET.action(do)
    PET.subtract()
    