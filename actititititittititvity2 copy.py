class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness
    def play(self, play):
        self.__happiness += 5
        print(f"Fluffy is playing {play}!")
    def show_status(self):
        print(self.__happiness)

Fluffy = Pet("Fluffy", 0)

Fluffy.show_status


""" Fluffy is playing fetch!
Fluffys happiness is now 10 """