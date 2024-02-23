alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Encrypt():
    encrypt_text= str()

    user_input = input("Enter Your Encryption Text: ").replace(" ", "").lower()

    for i in user_input:
        index = alphabet.index(i) 
        encrypt_text += alphabet[(index+3) % 26]

    return encrypt_text.upper()

def Decrypt():
    decrypt_text= str()

    user_input = input("Enter Your Cipher: ").lower()
   
    for i in user_input:
        index = alphabet.index(i) 
        decrypt_text += alphabet[(index-3) % 26]
        
    return decrypt_text.lower()

while True:
    print ("\n\nCeasar Cipher Encryption\n01. Press Number \"1\" for Encrypt Your Text.\n02. Press Number \"2\" for Decrypt Your Cipher.\n03. Press Number \"0\" for Exit.")
    try:
        Number = int(input("Enter Your Number: "))
    except:
        print("Please Enter Value Number And Try Again!")
        continue

    if Number == 0:
        exit()
    elif Number == 1:
        encryption = Encrypt()
        print(f"Cipher: \"{encryption}\"\nKey Value: 03 (defult Value)")
    elif Number == 2:
        decryption = Decrypt()
        print(f"Your Text: \"{decryption}\"")
    else:
        print("Please Enter Number Between 0-3!")
