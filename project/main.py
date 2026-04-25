from bank import Bank
from address import Address

banks = []

# sbi = Bank("State Bank of India","dadar","SBI0001")

# bob = Bank("State Bank of India","dadar","SBI0001")
# sbi.add_customer('prakash', 'singh','kshatreeya','singh@gmil.com','7000505020','saving')
#
# bob.add_customer('shiv', 'dev','prabhu','singh@gmil.com','7000505020','saving')
#
# sbi_customers = sbi.list_all_cunstomers()
#
# bob_customer = bob.list_all_cunstomers()
#
# print(sbi_customers)
#
# print(bob_customer)

start = True
while start:
    try:
        print('='*50)
        print('Choose Option (1-5): ')
        print('1: Add new bank')
        print('2: Net Banking')
        print('3: Create new Account')
        print('4: Remove Customer')
        print("5: Bank's Detail")
        print("6: Find Customer and bank details")
        print('7: Quite to system')

        choice = input("Enter Your choice: ")
        has_no = choice.isnumeric()
        if has_no:
            choice = int(choice)
            if choice == 1:
                """Register new Bank"""
                bank_name = input("\nEnter bank name: ")
                print('-'*50)
                branch_name = input("\nEnter Branch name: ")
                print('-'*50)
                ifsc_code = input("\nEnter Ifsc code: ")
                print('-'*50)

                bank = Bank(name=bank_name,branch=branch_name,ifsc=ifsc_code)

                banks.append(bank)
                # print(banks[0])
            if choice ==2:
                """Net banking services"""
                print('Select bank: ')
                print('-'*50)
                """display all bank in from the list"""
                for index in range(len(banks)):
                    print(f'Option:- {index} - {banks[index]}')

                selected = input("Please select an option : ")
                selected_no = selected.isnumeric()
                if selected_no:
                    selected = int(selected)
                    selected_bank =banks[selected]
                    customer_id = int(input("Enter customer id: "))

                    # for i in selected_bank._customer_details:
                    #     print(i.customer_id)
                    customer =[i for i in selected_bank._customer_details if i.customer_id == customer_id]
                    print(customer)
                # selection = True
                # while selection:
                    print('Select option:')
                    print("1: Cash Deposit")
                    print("2: Withdraw")
                    print("3: Money Transfer")
                    print("4: update Profile")
                    print("5: show Profile")
                    option = input("Please select any above otpion (1-4): ")
                    #check input is number or not
                    option_is_no = option.isnumeric()
                    # print(option_is_no)
                    if option_is_no:
                        #convert into integer 
                        option = int(option)
                        if option == 1:
                            amount = float(input("Enter deposit amount : "))
                            print(customer[0]._is_active)
                            customer[0].deposit(amount)
                            print(customer[0]._balance)
                        if option ==2:
                            amount = float(input("Enter withdral amount: "))
                            status = customer[0].withdraw(amount)
                            print(f'{'Transation Successfully' if status else status}')
                        if option ==3:
                            """display all bank in from the list"""
                            for index in range(len(banks)):
                                print(f'Option:- {index} - {banks[index]}')

                            selected = input("Please select i option : ")
                            selected_no = selected.isnumeric()
                            if selected_no:
                                selected = int(selected)
                                selected_bank =banks[selected]
                                print(selected_bank)
                                """take input to customer id"""
                                customer_id = int(input("Enter other customer id: "))
                                amount = float(input("Please Enter amount: "))
                                print(selected_bank._customer_details)
                                to_customer = None
                                for i in selected_bank._customer_details:
                                    print(i.customer_id)
                                    if i.customer_id == customer_id:
                                        to_customer = i


                                print(to_customer)
                                if to_customer:
                                    debit = customer[0].withdraw(amount=amount)
                                    if debit:
                                        credit = to_customer.deposit(amount=amount)
                                        if credit:
                                            print("Money Transfer successfully")

                        if option == 4:
                            street = input("street: ")
                            city = input("City : ")
                            state = input("State : ")
                            zip_code = input("Zip code : ")
                            address = None
                            if street and city and  state and  zip_code:
                                address = Address(street, city, state, zip_code)
                            else:
                                print("All field are required!")
                            
                            pan_card_no = input("Enter pan no.: ")
                            aadhar_card_no = input("Enter aadhar card no. : ")
                            dob = input("Enter Date of birth: ")
                            customer[0].update_details(address=address,dob=dob,aadhar_card_no=aadhar_card_no,pan_card_no =pan_card_no )
                            print(customer[0]._is_active)

                        if option == 5:
                        
                           profile =  customer[0].get_profile()
                           print(profile)
            if choice ==3:
                print('Select bank: ')
                print('-'*50)
                for index in range(len(banks)):
                    print(f'{index}: {banks[index]}')

                selected = input("Please select i option : ")
                selected_no = selected.isnumeric()
                if selected_no:
                    selected = int(selected)
                    selected_bank =banks[selected]
                    bank_name = selected_bank.name
                    print(f'You have selected {bank_name} bank')
                    #customer = ["first_name","middle_name","last_name","email","phone","account_type"]
                    print('-'*50)
                    first_name = input("Enter customer first_name: ")
                    print('-'*50)
                    middle_name = input("Enter customer middle_name: ")
                    print('-'*50)
                    last_name = input("Enter customer last_name: ")
                    print('-'*50)
                    email = input("Enter customer Email: ")
                    print('-'*50)
                    phone = input("Enter customer mobile no. : ")
                    print('-'*50)
                    account_type = input("Enter customer account type: ")
                    print('-'*50)
                    selected_bank.add_customer(first_name,middle_name,last_name,email,phone,account_type)
                    customers = selected_bank.list_all_cunstomers()
                    print(customers)
            if choice==4:
                print("Select bank")
                for index in range(len(banks)):
                    print(f'Option:- {index} - {banks[index]}')

                selected = input("Please select i option : ")
                selected_no = selected.isnumeric()
                if selected_no:
                    selected = int(selected)
                    selected_bank =banks[selected]
                    customer_id = int(input("Enter customer id to account cloase: "))
                    """search customer by id"""
                    for i in selected_bank._customer_details:

                        if customer_id == i.customer_id:
                            selected_bank._customer_details.remove(i)
                            print(f'{customer_id} id closed account')
                        else:
                            print(f'id {customer_id} not found! \nplease enter valied customer id')

            if choice == 5:
                print("Select bank : ")
                for index in range(len(banks)):
                    print(f'Opiton : {index} {banks[index]}')
                selected = input("Please select any option : ")
                selected_no = selected.isnumeric()
                if selected_no:
                    selected = int(selected)
                    bank = banks[selected]
                    bank.export_data()
            if choice == 6:
                print("Select bank: ")
                print('-'*20)
                for i in range(len(banks)):
                    print(f'Option {i} | {banks[i]}')
                selected = input("Please select an option: ")
                has_no = selected.isnumeric()
                if has_no:
                    """select bank from banks list"""
                    selected = int(selected)
                    selected_bank = banks[selected]

                    print('-'*30)
                    print("choose option: ")
                    print("1 : Find customer by id")
                    print("2 : Find customer by account number")
                    print("3 : Find customer by name")
                    print("4: Check Total Amount in bank")
                    option = int(input("Enter a number (1-3): "))
                    """Search customer by customer id"""
                    if option == 1:
                        customer_id = int(input("Search customer by id: "))
                        customer = selected_bank.find_by_id(customer_id)
                        print(f'{customer}')
                    """Search customer by account number"""
                    if option == 2:
                        acc_no = int(input("Search customer by account nunmber: "))
                        customer = selected_bank.find_by_acc_no(acc_no)
                        print(f'{customer}')
                        """search customers by name """
                    if option == 3:
                        name = input("Search customer by name: ")
                        customers = selected_bank.search_by_name(name)

                        for customer in customers:
                            print(f'{customer}')
                    if option == 4:
                        amount = selected_bank.total_deposits()
                        print(f'{selected_bank.name} total amount {amount}')
            if choice == 7:
                print("thanks for using us!")
                break

    except Exception as e:
        print(e)