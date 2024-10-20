# user
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.is_logged_in = False

    def login(self, email, password):
        if self.email == email and self.password == password:
            self.is_logged_in = True
            print(f"{self.name} has logged in.")
        else:
            print("Invalid email or password.")
    
    def logout(self):
        if self.is_logged_in:
            self.is_logged_in = False
            print(f"{self.name} has logged out.")
        else:
            print(f"{self.name} is not logged in.")

# إuser
user1 = User("Anas", "anas@example.com", "password123")
user1.login("anas@example.com", "password123")
user1.logout()
