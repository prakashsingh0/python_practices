from address import Address
import datetime
from csv import reader,DictWriter, writer,DictReader

class Customer:
    def __init__(self,first_name:str,middle_name:str,last_name:str,email:str,phone:str,account_type:str,account_number:str,customer_id:str,_balance = 0):
        self.customer_id = customer_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.account_type = account_type
        self.address = None
        self.dob = None
        self.aadhar_card_no = None
        self.pan_card_no = None
        self.account_number = account_number
        self._balance = _balance
        self._is_active = False
        self.transactions = []



    def __str__(self):
        return f"""\nCustomer ID: {self.customer_id}
\nAccount number : {self.account_number}
\nName : {self.first_name} {self.middle_name} {self.last_name}
\nAccount Status : {'Active' if self._is_active else "Deactive"}"""
    

    """update customer Profile details"""
    def update_details(self,address=None,dob=None,aadhar_card_no=None,pan_card_no = None):
        """Validate data"""
        if dob is not None:     
            self.dob = dob
        if address is not None:
            self.address = address
        if aadhar_card_no is not None:
            self.aadhar_card_no = address
        if pan_card_no is not None:
            self.pan_card_no  = pan_card_no
        if self.aadhar_card_no:
            self._is_active = True

            
    """show customer information"""    
    def get_profile(self):
        print('*'*50)
        print(f'Customer ID: {self.customer_id}')
        print(f'Account number : {self.account_number}')
        print(f'Account Type : {self.account_type}')
        print(f'Name : {self.first_name} {self.middle_name} {self.last_name}')
        print(f'Account balance : {self._balance}')
        print(f'Phone Number : {self.phone}')
        print(f'Address : {self.address.format_address()
                           }')

        print(f'Account Status : {'Active' if self._is_active else "Deactive"} ')
        print(f'statement : \n {self.transactions}')


        print('*'*50)


    """Deposit amount"""
    def deposit(self,amount:float):
        try:
          if self._is_active:
            if amount <= 0 :
                raise ValueError("Amount must be Greater then 0")
            if amount >= 0:
                self._balance += amount
                date_today = datetime.datetime.now().strftime("%y-%m-%d")
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                self.transactions.append({"Date":date_today, "time":current_time, "status":"Credit", "Amount":amount})
                return True
          else:
              print('Your Account is not Activated')
        except Exception as e:
            print(f'Something went wrong {e}')
    """Withdraw cash from account"""
    def withdraw(self,amount):
        try:
            if amount > self._balance:
                raise ValueError("Insufficient funds")
            if amount <= 0:
                raise ValueError("Amount must be greater then 0")
            if amount <= self._balance and amount >= 0:
                self._balance -= amount
                date_today = datetime.datetime.now().strftime("%y-%m-%d")
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                self.transactions.append({"Date":date_today, "time":current_time, "status":"Debit", "Amount":amount})
                return True
        except Exception as e:
           print(f'Something went wrong {e}')
    
    # def transfer(amount, to_customer:id):
    #     debit = withdraw(amount)
    #     if debit:
    #         deposite()
    #     pass

    def get_statement(self):
        #return csv file
        file_name = self.first_name
        with open(f'{file_name}_statement.csv','w') as file:
            header = ["Date","time","status","Amount"]
            csv_writer = DictWriter(file, fieldnames=header)
            csv_writer.writeheader()

            for statement in self.transactions:
                csv_writer.writerow({
                    "Date":statement['Date'],
                    "time":statement['time'],
                    "status":statement['status'],
                    "Amount":statement['Amount']
                })
        return f'Statement downloaded by name {file_name+'statement.csv'}'
        
