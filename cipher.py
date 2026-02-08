# Cipher encoding and decoding
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(original_txt,shifted_amount):

    text=""
    for char in original_txt:
        shift=alphabet.index(char) + shifted_amount

        shift%=len(alphabet)

        text+=alphabet[shift]

    print(f"Your encoded message is {text}")
        

def decrypt(original_txt,shifted_amount):
    
    text=""
    for char in original_txt:
        shift=alphabet.index(char) - shifted_amount

        shift%=len(alphabet)

        text+=alphabet[shift]

    print(f"Your decoded message is {text}")

should_continue =True
while should_continue:
    
    msg=input(f"TYPE encode for encryption and decode for decryption.\n")
    code=input("Enter your message:")
    shifted=int(input("Enter your shift number:"))
    
    if msg=="encode":
        encrypt(original_txt=code,shifted_amount=shifted)
    else:
        decrypt(original_txt=code,shifted_amount=shifted)
    
    user=input(f"TYPE yes if you want to go again. Otherwise NO\n")
    if user=="no":
         should_continue=False
         print("Goodbye.")
    
    
         





    
    









