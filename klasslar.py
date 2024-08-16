class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email


    def describe(self):
        return f"Ismi: {self.name}, Foydalanuvchining nomi: {self.username}, Pochtasi: {self.email}"


user1 = User("Diyorbek", "diyor089" , "diyor@52gmail.com")
print(user1.describe())