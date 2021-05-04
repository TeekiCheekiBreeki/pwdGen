import random
import string
import PySimpleGUI as sg
filename = r'C:\Users\teeki\Documents\Passwords\passwords.txt'
def generate_password(account, length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    #All possible symbols to be used in password
    all_symbols = lower + upper + num + symbols
    #we generate <length> long password and print it out
    temp = random.sample(all_symbols,length)
    password = "".join(temp)

    return password

def new_password():
    

    layout = [
        [sg.Text("Password Account"), sg.Input(key='account')],
        [sg.Text("Password Length "), sg.Input(key='length' )],
        [sg.Button("Generate"), sg.Text("", size=(0, 1), key='password')],
    ]
    window = sg.Window('New Password', layout, modal=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Generate":
            account = values['account']
            length = int(values['length'])
            password = generate_password(account, length)
            text_file = open(r'C:\Users\teeki\Documents\Passwords\passwords.txt' , 'a')
            n = text_file.write('\n' + account + ' password: ' + password)
            text_file.close()
            if password:
                window['password'].update(value=password)
            else:
                window['password'].update(value='')
    window.close()

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


