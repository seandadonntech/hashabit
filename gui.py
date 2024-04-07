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

def write_to_file(text, hash_functions):
    with open('hashed_out.txt', 'w') as file:
        for hash_function in hash_functions:
            file.write(f'{hash_function.__name__} Hash: {hash_function(text)}\n')

layout = [
    [sg.Text("Enter text to convert to hash:")],
    [sg.InputText(key='-INPUT-')],
    [sg.Button('SHA256'), sg.Button('SHA1'), sg.Button('Blake2b'), sg.Button('Write to File')],
    [sg.Output(size=(50,10))]
]

window = sg.Window('Hashabit', layout)
hash_functions = []

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    text = values['-INPUT-']
    if event == 'SHA256':
        print(f'Text: {text}')
        print(f'SHA256 Hash: {sha256(text)}')
        hash_functions.append(sha256)
    elif event == 'SHA1':
        print(f'Text: {text}')
        print(f'SHA1 Hash: {sha1(text)}')
        hash_functions.append(sha1)
    elif event == 'Blake2b':
        print(f'Text: {text}')
        print(f'Blake2b Hash: {blake2b(text)}')
        hash_functions.append(blake2b)
    elif event == 'Write to File':
        if hash_functions:
            if text:
                write_to_file(text, hash_functions)
            else:
                print("Please enter some text before writing to file.")
        else:
            print("Please select at least one hash function before writing to file.")
        
window.close()
