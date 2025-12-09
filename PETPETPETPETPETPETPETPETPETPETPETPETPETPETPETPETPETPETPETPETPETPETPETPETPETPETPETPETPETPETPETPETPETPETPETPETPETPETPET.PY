class Pet:
    def __init__(self, name, hungry, thirsty, happy, age, tired):
        self.name__ = name
        self.hungry__ = hungry
        self.thirsty__ = thirsty
        self.happy__ = happy
        self.age__ = age
        self.tired__ = tired
    
    def feed(self):
        return (f"Your pet is %{self.hungry} hungry")

