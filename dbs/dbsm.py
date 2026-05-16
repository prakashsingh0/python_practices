import pymongo

from pprint import pprint

client = pymongo.MongoClient()
db = client["python_test_users"]

users_coll = db["users"]


class Users:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone


    # @staticmethod
    def login(email):
        user = users_coll.find_one({"email":email})
        if user:
            print(f'Welcome {user['name']}')







users_data =[
    {
        "first_name":"prakash",
        "last_name":"singh",
        "age":10,
        "email":"singh@gmail.com"
    },
    {
        "first_name":"prakash",
        "last_name":"singh",
        "age":10,
        "email":"singh@gmail.com"
    },
    {
        "first_name":"prakash",
        "last_name":"singh",
        "age":10,
        "email":"singh@gmail.com"
    },
    {
        "first_name":"prakash",
        "last_name":"singh",
        "age":10,
        "email":"singh1@gmail.com"
    }]

"""insert data"""
# users_coll.insert_one(users_data[0])
# users_coll.insert_many(users_data)
name = input('Please enter your name ')
email = input("please enter your  email: ")
# phone = input("Please enter your number: ")

# def register(name,email,phone):
#     if not name and not email and not phone:
#         return ({"message":"all field are required"})
#     else:
#         user = Users(name,email,phone)
#         print(user)
#         users_coll.insert_one({"name":user.name,"email":user.email,"phone":user.phone})


# register(name,email,phone)
Users.login(email)
"""find users"""
all_users = list(users_coll.find())

for user in all_users:
    pprint(user)
pprint(len(all_users))

