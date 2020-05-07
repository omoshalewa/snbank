import random


def verify_details():
    login = True

    selection = input('''What would you like to do?
            Type 'y' for Staff login or 'n' to Close app: ''').lower()
    while login == True:
        if selection == 'y':
            print('Kindly provide login details')
            username = input('Username: ').lower()
            password = input('Password: ').lower()
            file = open("staff.txt", "r")
            for row in file:
                field = row.split(',')
                staff_name = field[0]
                staff_pw = field[1]
                if username == staff_name and password == staff_pw:
                    print('Successful Login')
                    login = False
                    break

            else:
                print('Invalid details')

        else:
            print('Your session has been terminated')
            exit()


def account_creation():
    option = True

    while True:
        option = input("""Type '1' To Create New Bank Account 
        '2' To Check Account Details 
        '3' To Logout\nSelect an option: """)
        if option == '1':
            print('Kindly Provide The Following Details')
            alc_name = input('Account Name: ')
            open_bal = input('Opening Balance: ')
            alc_type = input('Account Type: ')
            alc_email = input('Account Email: ')

            alc_no = random.randint(1000000001, 1999999998)
            print(f'Your Account number is {alc_no}')

            file_name = 'customer.txt'
            with open(file_name, 'a') as file_object:
                file_object.write(str(alc_no))
                file_object.write(',')
                file_object.write(alc_name)
                file_object.write(',')
                file_object.write(open_bal)
                file_object.write(',')
                file_object.write(alc_type)
                file_object.write(',')
                file_object.write(alc_email)
                file_object.write('\n')

        elif option == '2':
            account_no = input('Kindly Provide Your Account Number: ')
            file = open("customer.txt", "r")
            for row in file:
                field = row.split(',')
                acct_no = field[0]
                if account_no == acct_no:
                    print(field)
                    break
            else:
                print('Invalid details')

        elif option == '3':
            verify_details()
            option = False

        else:
            print('Pick a valid option\n1, 2, 0r 3')


def banking_system():
    verify_details()
    account_creation()


banking_system()