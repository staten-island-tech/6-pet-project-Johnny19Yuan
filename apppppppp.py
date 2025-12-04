class Teacher():
    def __init__(self, name, email, subject):
        super().__init__(name)
        self.subject = subject
    def display_info(self):
        base_info = super().display_info()
        return (f"{base_info}, Subject: {self.subject}")
mr_walen = Teacher("mr_walen","mrwalen@proton.me","com_sci")
print(Teacher.display_info)