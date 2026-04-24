from customer import Customer
from csv import reader, DictReader,DictWriter,writer


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
    def export_data(self):
        file_name = self.name
        with open(f'{file_name}.csv','w') as file:
            header = ["first_name","middle_name","last_name","email","phone","account_type","address","dob","aadhar_card_no","pan_card_no","account_number","_balance","_is_active"]
            csv_writer = DictWriter(file,fieldnames=header)
            csv_writer.writeheader()
            
            for customer in self._customer_details:
                csv_writer.writerow(
                    {"first_name":customer.first_name,"middle_name":customer.middle_name,"last_name":customer.last_name,"email":customer.email,"phone":customer.phone,"account_type":customer.account_type,"address":customer.address,"dob":customer.dob,"aadhar_card_no":customer.aadhar_card_no,"pan_card_no":customer.pan_card_no,"account_number":customer.account_number,"_balance":customer._balance,"_is_active":customer._is_active}
                    )
                print(f'file export successfully file name : {file_name+'.csv'}')