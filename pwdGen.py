import random
import string
import PySimpleGUI as sg

layout = [[sg.Text("Welcome to Password Generator")], [sg.Button("Exit")], [sg.Button("Password List")],[sg.Button("New Password")]]
window = sg.Window("Password Generator", layout)
while True:
    event, values = window.read()
    
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
window.close()

print("For which account you want your password: ")

account = input();
with open(r'C:\Users\teeki\Documents\Passwords\passwords.txt') as file:
    content = file.readlines

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
