walen = str("walen")

class Teacher(walen):
    
    def __init__(self, name,email, subject):
        
        super().__init__(name, email, subject)
        self.name = name
        self.email = email
        self.subject = subject
    
    def display_info(self):
        print(Teacher.display_info)
mr_walen = Teacher("mr_Whalen","mrwalen@proton.me","com sci")
