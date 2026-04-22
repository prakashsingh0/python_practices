from customer import Customer



class Bank:

    def __init__(self,name:str,branch:str,ifsc:str):
        self.name = name
        self.initials = None
        self.branch = branch
        self.ifsc = ifsc
        self._customer_details = []
        self.phone_nos = []
        self.address = {}
        self._next_id = 1
        self.next_account_number = 1
    

    def __str__(self):
        return f'{self.name} | {self.branch} | {self.ifsc}'

    def add_customer(self,first_name:str,middle_name:str, last_name:str,email:Str,phone:str,account_type:str):
        customer = Customer(first_name,middle_name,last_name,email,phone,account_type,account_number=self.next_account_number,customer_id=self._next_id)
        self._next_id += 1  
        self.next_account_number += 1
        self._customer_details.append(customer)
        # print(customer.customer_id)
        # print(f'bank all customer {self._customers[0]}')
        
    
    def remove_customer(self):
        pass

    def find_by_id(self):
        pass
    
    def find_by_acc_no(self,acc_no:str):
        pass
    def search_by_name(self,name:str):
        pass

    def list_all_cunstomers(self):
        return self._customer_details
        
    
    def total_deposits(self):
        pass
    
    def get_stats(self):
        pass