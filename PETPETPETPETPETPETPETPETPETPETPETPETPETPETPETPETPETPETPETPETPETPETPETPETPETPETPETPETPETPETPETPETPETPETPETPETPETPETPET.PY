class Pet:
   def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness
        
        def show(self,):
            print (f"{self.__name} is %{self.hungry} hungry")
            print (f"{self.name} is %{self.thirsty} thirsty")
            print (f"{self.name} is %{self.happy} happy")
            print (f"{self.name} is {self.age} days old")
            print (f"{self.name} is %{self.tired} tired")

Pet("Luke","0")

Pet.show(1)