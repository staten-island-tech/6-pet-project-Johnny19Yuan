class Pet:
    def __init__(self, name, hungry, thirsty, happy, age, tired):
        self.__name = name
        self.hungry = hungry
        self.thirsty = thirsty
        self.happy = happy
        self.age = age
        self.tired = tired
    
    def show(self,show):
        print (f"{self.__name} is %{self.hungry} hungry")
        print (f"{self.name} is %{self.thirsty} thirsty")
        print (f"{self.name} is %{self.happy} happy")
        print (f"{self.name} is {self.age} days old")
        print (f"{self.name} is %{self.tired} tired")

Pet("Luke","0","0","50","0","0")

Pet.show(1)