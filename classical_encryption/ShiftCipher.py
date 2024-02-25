alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Encrypt(user_input,shift=3):
    encrypt_text= str()
    if shift < 2 or shift > 25:
        return None
    
    for i in user_input:
        index = alphabet.index(i) 
        encrypt_text += alphabet[(index+shift) % 26]

    return encrypt_text.upper()

def Decrypt(user_input,shift=3):
    decrypt_text= str()

    if shift < 2 or shift > 25:
        return None
    
    for i in user_input:
        index = alphabet.index(i) 
        decrypt_text += alphabet[(index-shift) % 26]
        
    return decrypt_text.lower()

while True:
    print ("\n\nCeasar Cipher Encryption\n01. Press Number \"1\" for Encrypt Your Text.\n02. Press Number \"2\" for Decrypt Your Cipher.\n03. Press Number \"0\" for Exit.")
    try:
        Number = int(input("Enter Your Number: "))
    except:
        print("Please Enter Value Number And Try Again!")
        continue

    if Number == 0:
        break

    elif Number == 1:

        user_input = input("Enter Your Encryption Text: ").replace(" ", "").lower()

        try:
            shift_value = int(input("Enter Key Value Between 2 - 25: "))
        except:
            print("Please Enter Value Number Between 2 - 25 And Try Again!")
            continue

        encryption = Encrypt(user_input, shift_value)
        print(f"Cipher: \"{encryption}\"\nKey Value: {shift_value}")

    elif Number == 2:

        user_input = input("Enter Your Cipher: ").lower()

        try:
            shift_value = int(input("Enter your key (Defult value is 3): "))
        except:
            print("Please Enter Value Number Between 2 - 25 And Try Again!")
            continue

        decryption = Decrypt(user_input, shift_value)
        print(f"Your Text: \"{decryption}\"")
    else:
        print("Please Enter Number Between 0-3!")