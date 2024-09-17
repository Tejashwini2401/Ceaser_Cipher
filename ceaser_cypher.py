letters = 'abcdefghijklmnopqrstuvwxyz'
num = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == "d":
        key = -key
    for letter in text:
        letter = letter.lower()
        if not letter == '':
            index =letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num:
                    new_index -= num
                elif new_index < 0:
                    new_index += num
                result += letters[new_index]
    return result

print()
print("CEASER CYPHER\n")

while(True):

    print("Do you want to encrypt or decrypt??")
    usrip = input("e or d\n").lower()

    if usrip == 'e':
        print("Encryption mode selected\n")
        while(True):
            key = int(input("Enter the key (1-26): "))
            if key>0 and key<27:
                text = input("Enter the text to encrypt: ")
                ciphertext = encrypt_decrypt(text, usrip, key)
                print("CIPHER TEXT: ", ciphertext)
                break
            else:
                print("Enter number between 1 and 26")
                continue

    elif usrip == 'd':
        print("Decryption mode selected\n")
        while(True):
            key = int(input("Enter the key (1-26): "))
            if key<27 and key>0:
                text = input("Enter the text to decrypt: ")
                plaintext = encrypt_decrypt(text, usrip, key)
                print("PLAIN TEXT: ", plaintext)
                break
            else:
                print("Enter number between 1 and 26")
                continue

    elif usrip == 'q':
        break
    
    else:
        print("Please enter appropriate mode")
        continue

