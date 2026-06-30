class CaesarCipher:

    def __init__(self, key):
        self.key = key % 26


    def encrypt(self, text):

        result = ""

        for char in text:

            if char.isupper():
                result += chr((ord(char)-65+self.key)%26+65)

            elif char.islower():
                result += chr((ord(char)-97+self.key)%26+97)

            else:
                result += char

        return result



    def decrypt(self,text):

        result=""

        for char in text:

            if char.isupper():
                result += chr((ord(char)-65-self.key)%26+65)

            elif char.islower():
                result += chr((ord(char)-97-self.key)%26+97)

            else:
                result += char

        return result
