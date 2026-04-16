#chat application

class User:
    def __init__(self,name,phone,passward,messages=[],status='offline'):
        self.name = name
        self.phone = phone
        self.passward = passward
        self.message = []
        self.status = status

    def login(self,phone,passward):
        try:
            
            phone = phone.strip()
            passward = passward.strip()
            if not phone:
                raise ValueError('phone can\'t be empty')
            elif not passward:
                raise ValueError('Passward can\'t be empty')
            if phone == self.phone and passward == self.passward:
                print(f'Welcome, {self.name} !')
                self.status = 'online'
            else:
                return 'Please enter valid cradential'

        except Exception as e:
            print(e)

    def register(self,name,phone,passward):
        try:
            phone = phone.strip()
            passward = passward.strip()
            if not phone and not passward :
                raise ValueError('all fiend are required')
            else:
                if len(phone) == 10:
                    self.name = name
                    self.passward = passward
                    print('Account created successfully')
                else:
                    raise ValueError('enter 10 digit phone')
        except Exception as e:
            print(e)

    def _chat(self,phone,text):
        hkj


user1 = User('prakash','7000505020','test@123')
user1.register('prakash','7000505020','test@123')
print(user1.name)
print(user1.phone)
print(user1.message)
print(user1.status)
user1.login('7000505020','test@123')
print(user1.status)
