import random
import string
import PySimpleGUI as sg
filename = r'C:\Users\teeki\Documents\Passwords\passwords.txt'

def new_password():
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


def popup_text(filename, text):

    layout = [
        [sg.Multiline(text, size=(80, 25)),],
    ]
    win = sg.Window(filename, layout, modal=True, finalize=True)

    while True:
        event, values = win.read()
        if event == sg.WINDOW_CLOSED:
            break
    win.close()

sg.theme('LightBlue3')
layout = [[sg.Text("Welcome to Password Generator")], [sg.Button("Exit")], [sg.Button("Password List"), sg.Button("New Password")]]
window = sg.Window("Password Generator", layout)


while True:
    event, values = window.read()
    
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Password List":
        with open(filename, "rt", encoding='utf-8') as f:
            text = f.read()
            popup_text(filename, text)
    elif event == "New Password":
        new_password()       
window.close()


