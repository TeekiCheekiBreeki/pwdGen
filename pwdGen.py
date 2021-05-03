import random
import string
#implementing this later

print("For which account you want your password: ")

account = input();


length = int(input('\nHow long do you want your password to be: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#All possible symbols to be used in password
all_symbols = lower + upper + num + symbols
#we generate <length> long password and print it out
temp = random.sample(all_symbols,length)
password = "".join(temp)


# We save password to the passwords.txt
text_file = open(r'C:\Users\teeki\Documents\Passwords\passwords.txt' , 'a')
n = text_file.write('\n' + account + ' password: ' + password)
text_file.close()

print("Your password is: ", password)
