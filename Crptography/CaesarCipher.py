'''
ord -- char to ascii code
chr -- ascii code to char

    -->65 is A 97 is a
    -->Total alphabate is 26
'''
def encrypt(string, shift):
    cipher = ''
    for char in string:
        if char == " ":
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher
def decrypt(string, shift):
    cipher = ''
    for char in string:
        if char == " ":
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
    return cipher

def main():
    while True:

        mode = input('''
        Press 1 to Encrypt  :
        Press 2 to Decrypt  :
        Press q to quit     :
                    ''' )
        if mode == '1' :
            en_text = str(input("Enter the text to encrypt : "))
            en_key = int(input("Enter the no of shift : "))
            print("Your encrypted text is : ", encrypt(en_text, en_key))
        elif mode == '2':
            de_text = str(input("Enter the text to decrypt : "))
            de_key = int(input("Enter the no of shift : "))
            print("Your encrypted text is : ", decrypt(de_text, de_key))
        elif mode == 'q':
            print("\n\tKeep Safe ")
            break
        else:
            continue
if __name__ == "__main__":
    main()