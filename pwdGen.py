import random
import string
#implementing this later

#print("For which account you want your password: ")

#account = input();


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

print("Your password is: ", password)
