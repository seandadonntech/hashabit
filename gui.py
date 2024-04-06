import hashlib
import PySimpleGUI as sg

def sha256(text):
    hash_object = hashlib.sha256(text.encode())
    return hash_object.hexdigest()

def sha1(text):
    hash_object = hashlib.sha1(text.encode())
    return hash_object.hexdigest()

def blake2b(text):
    hash_object = hashlib.blake2b(text.encode())
    return hash_object.hexdigest()

layout = [
    [sg.Text("Enter text to convert to hash:")],
    [sg.InputText(key='-INPUT-')],
    [sg.Button('SHA256'), sg.Button('SHA1'), sg.Button('Blake2b')],
    [sg.Output(size=(50,10))]
]

window = sg.Window('Hashabit', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    text = values['-INPUT-']
    if event == 'SHA256':
        print(f'Text: {text}')
        print(f'SHA256 Hash: {sha256(text)}')
    elif event == 'SHA1':
        print(f'Text: {text}')
        print(f'SHA1 Hash: {sha1(text)}')
    elif event == 'Blake2b':
        print(f'Text: {text}')
        print(f'Blake2b Hash: {blake2b(text)}')

window.close()

