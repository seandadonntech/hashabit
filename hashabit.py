import hashlib

def sha256():
    text = input("Enter text to convert to SHA256 hash: ")
    hash_object = hashlib.sha256(text.encode())
    print(f'Text: {text}')
    print(f'SHA256 Hash: {hash_object.hexdigest()}')


    
# end def



options = input("Enter 1:")

if options == "1":
 sha256()



elif options == " ":
 print("")
 # 
 