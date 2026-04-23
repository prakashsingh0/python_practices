from bank import Bank

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
    print('='*50)
    print('Choose Option (1-5): ')
    print('1: Add new bank')
    print('2: Net Banking')
    print('3: Create new Account')
    print('4: Remove Customer')
    print("5: Update Customer Profile")

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
            
            selected = input("Please select i option : ")
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
                print("1: Cash Diposit")
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
                        print('option 1')
                        print(customer[0]._is_active)
                        customer[0].diposit(100)
                        print(customer[0]._balance)
                    if option ==2:
                        print('option 1')
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
                            
                            # to_customer = [i for i in selected_bank._customer_details if i.customer_id == customer_id]
                            print(to_customer)
                            if to_customer:
                                debit = customer[0].withdraw(amount=amount)
                                if debit:
                                    credit = to_customer.diposit(amount=amount)
                                    if credit:
                                        print("Money Transfer successfully")
        
                    if choice == 4:
                        customer[0].update_details(aadhar_card_no='987976')
                        print(customer[0]._is_active)
                    if choice ==5:
                        customer[0].get_profile()

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
            start = False

