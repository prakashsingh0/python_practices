# Create a contact book using dict.

contacts = {}

while True:
    print('='*50)
    print('Choose Option (1-5): ')
    print('1.Add Contact')
    print('2.Delete contact'.title())
    print('3.delete all contacts'.title())
    print('4.show contacts'.title())
    print('5.Quit')
    print('='*50)
   
    choice = input('Enter Your choice: ')
    has_num = choice.isnumeric()
    
    if has_num:
        choice = int(choice)
    
        if choice == 1:
            print('Add new contact')
            name = input('Enter name: ').lower()
            print('-'*20)

            if name not in contacts:
                phone = input('Enter number: ')
                contacts[name] = phone
                print(f'Contact added {name}: {phone}')
            else:
                print(f'Name {name} alreay have in contacts')
        elif choice == 2:
            print('Delete contact')
            name = input('Enter name: ').lower()
            if name in contacts:
                print('-'*20)
                deleted =  contacts.pop(name)
                print(f'Deleted {name} : {deleted} successfully')
                print('-'*20)
            else:
                print(f'Contact not exist {name}')
        elif choice == 3:
            option = input('are you sure (yes/no): ').lower()
            if option == 'yes':
                contacts.clear()
            else:
                print('-'*20)
                print('Cancelled deletion contacts'.title())
        elif choice == 4:
            print('-'*20)
            if len(contacts)>0:

                for name, phone in contacts.items():
                    print(f'{name}: {phone}')
            else:
                print(f'Contact List Empty {len(contacts)}')
                print('-'*20)
        elif choice == 5:
            print('-'*20)
            print('GoodBye...')
            break
        else:
            print('Please Enter a valid choice')
    else:
        print('please enter number only')