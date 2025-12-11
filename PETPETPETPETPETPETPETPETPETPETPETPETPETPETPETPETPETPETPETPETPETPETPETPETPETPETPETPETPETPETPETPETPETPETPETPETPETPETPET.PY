class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness
    def show(self):
        print (f"{self.name} is %{self.__happiness} hungry")

Luke = Pet("Luke","0")

Luke.show()