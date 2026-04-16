class Users:
    def __init__(self,first_name, last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    def login(self):
        if self.email or self.password:
            return f'Welcome {self.first_name}'


user1 = Users('prakash','singh','singh@gamil.com','test@123')
message = user1.login()

user2 = Users('shivam','singh','shivam@gamil.com','test@123')

print(user1.first_name)
print(message)
print(user2.first_name)
print(user2.email)
print(user2.login())
        