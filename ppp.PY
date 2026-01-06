import time

class Pet:
    def __init__(self, name, hungry, happy, age, tired, alive):
        self.__name = str(name)
        self.__hungry = int(hungry)
        self.__happy = int(happy)
        self.__age = int(age)
        self.__tired = int(tired)
        self.alive = bool(alive)
    
    def show(self):
        if (self.__happy <= 0) or (self.__tired >= 100) or (self.__hungry <= 0):
            self.alive = False
            
        
        print (f"{self.__name} is {self.__hungry} full, {self.__happy} happy, {self.__tired}% tired, and {self.__age} days old")

    def action(self, do):
        if do == "Play":
            self.__happy += 25
            self.__age += 0.1
            print(f"{self.__name} is playing...")
            time.sleep(5)
        elif do == "Feed":
            self.__hungry += 25
            self.__age += 0.1
            print(f"{self.__name} is eating...")
            time.sleep(5)
        elif do == "Sleep":
            self.__tired = -20
            self.__age += 0.2
            print(f"{self.__name} is sleeping...")
            time.sleep(10)
        
    def subtract(self):
        self.__happy -= 10
        self.__hungry -=10
        self.__tired += 20
petname = input("Name your pet: ")
petstats = Pet(f"{petname}","50","50","0","0","True")
while Pet.alive == True:
    petstats.show()
    do = input("What to do with pet? Play, Feed, or Sleep? ")
    petstats.action(do)
    petstats.subtract()