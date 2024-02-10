import hashlib

def sha256():
    text = input("Enter text to convert to SHA256 hash: ")
    hash_object = hashlib.sha256(text.encode())
    print(f'Text: {text}')
    print(f'SHA256 Hash: {hash_object.hexdigest()}')
   

def sha1():
   text = input("Enter text to convert SHA1 hash")
   hash_object = hashlib.sha1(text.encode())
   print(f'Text: {text}')
   print(f'SHA1 Hash: {hash_object.hexdigest}')
   
   
   
   
def help():
 print("welcome to hasabit Enter 1 for sha256, 2 for sha1, 3 for help")

    # end def






options = input("Enter options: ")

if options == "1":
 sha256()



elif options == "2":
 print("Please enter")
 
 
 
else:
 print("Invalid option")
 help()
 
 





