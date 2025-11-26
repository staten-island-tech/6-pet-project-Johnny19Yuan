class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness
    def play(self, play):
        self.__happiness += 10
        print(f"{self.name} is playing {play}!")
    def show_status(self,show):
        print(f"{self.name}'s happiness is now {self.__happiness}")

Fluffy = Pet("Fluffy", 0)
play = True
while play == True:
    Fluffy.play(input("Fluffy"))
    Fluffy.show_status(1)


""" Fluffy is playing fetch!
Fluffys happiness is now 10 """