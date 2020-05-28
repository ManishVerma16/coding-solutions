import os          # to import os module for running bash cmd.

os.system('tput setaf 1')   # to change color of font to red
print('\t\t\t Welcome To My TUI thats makes life simple')
os.system('tput setaf 7')   # to change color of font to white
print('\t\t\t-----------------------------------------')

print('would you like to perform your job (local/remote): ', end='')
locationchoice = input()
if locationchoice == 'remote':
    ipAddress = input('Enter ip address: ')
    pingresult = os.system('ping {}'.format(ipAddress))


print('''
Press 1: to see date
Press 2: to check cal
Press 3: to configure webserver
Press 4: to create user
Press 6: to setup networking
Press 7: to exit
''')


print("Enter your choice: ", end='')      # end is default arg with value \n and change it accordingly.
ch = input()

if locationchoice == 'local':
    if int(ch) == 1:
        os.system('date')
    elif int(ch) == 2:
        os.system('cal')
    elif int(ch) == 3:
        os.system('yum install httpd')
    elif int(ch) == 4:
        userName = input('Enter username: ')
        password = input('Enter your password: ')
        os.system('useradd {}'.format(userName))
    elif int(ch) == 7:
        exit
    else:
        print('option not supported')

elif locationchoice == 'remote':
    if int(ch) == 1:
        os.system('ssh {} date'.format(ipAddress))
    elif int(ch) == 2:
        os.system('ssh {} cal'.format(ipAddress))
    elif int(ch) == 3:
        os.system('ssh {} yum install httpd'.format(ipAddress))
    elif int(ch) == 4:
        userName = input('Enter username: ')
        password = input('Enter your password: ')
        os.system('ssh {} useradd {}'.format(ipAddress,userName))
    elif int(ch) == 7:
        exit
    else:
        print('option not supported')

else:
    print('Location does not supported')

