from encryption.cipher import CaesarCipher
from database.db import *
import random


create_db()


print("""
=========================
 DecodeLabs Secure System
=========================
""")


while True:


    print("""
1. Encrypt Message
2. Decrypt Message
3. Exit
""")


    choice=input("Enter choice: ")


    if choice=="1":

        msg=input("Enter message: ")

        key=random.randint(1,25)

        cipher=CaesarCipher(key)

        encrypted=cipher.encrypt(msg)


        print("\nKey:",key)
        print("Encrypted:",encrypted)


        save_message(encrypted)



    elif choice=="2":

        msg=input("Enter encrypted message: ")

        key=int(input("Enter key: "))


        cipher=CaesarCipher(key)


        print(
        "Decrypted:",
        cipher.decrypt(msg)
        )


    elif choice=="3":

        break


    else:

        print("Wrong choice")

