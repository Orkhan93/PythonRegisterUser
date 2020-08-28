class User:
    def __init__(self):
        self.name="Orxan"
        self.surname="mustafayev"
    def showData(self):
        print(f" {self.name}  {self.surname}")

class AdminUser(User):
    def __init__(self):
        User.__init__(self)
        self.role="Admin"
    def showData(self):
        print(f"{self.name} {self.surname}  {self.role}")
yeni=User()
yeni.showData()

admin=AdminUser()
admin.showData()
