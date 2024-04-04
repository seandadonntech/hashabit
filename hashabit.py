import hashlib

def sha256():
    text = input("Enter text to convert to SHA256 hash: ")
    hash_object = hashlib.sha256(text.encode())
    print(f'Text: {text}')
    print(f'SHA256 Hash: {hash_object.hexdigest()}')

def sha1():
    text = input("Enter text to convert to SHA1 hash: ")
    hash_object = hashlib.sha1(text.encode())
    print(f'Text: {text}')
    print(f'SHA1 Hash: {hash_object.hexdigest()}')

def help():
    print("Welcome to hasabit. Enter 1 for SHA256, 2 for SHA1, 3 for help")

while True:
    help()
    option = input("ENTER OPTION: ")
    if option == "1":
        sha256()
    elif option == "2":
        sha1()
    elif option == "3":
        help()
    else:
        print("Invalid option. Please try again.") 