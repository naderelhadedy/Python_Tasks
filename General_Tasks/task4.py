# encrypt password and takes key amount to shift and prompts user to input password
def encrypt_password(key):

    password = input("Enter password: ")

    result = ""

    for letter in password:
        result += chr(ord(letter) + key)

    print(f"\nEncrypted Password: {result}\nKey: {key}\n")


# decrypt password and prompts user to result and key
def decrypt_password():

    password = input("Enter result: ")
    key = int(input("Enter key: "))

    result = ""

    for letter in password:
        result += chr(ord(letter) - key)

    print(f"\nPassword: {result}\n")



# call functions

encrypt_password(2)

decrypt_password()