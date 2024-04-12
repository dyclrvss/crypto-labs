def vCipher():
    print("enter 1 to encode a message")
    print("enter 2 to decode a message")
    print("enter 3 to quit")
    userSelection = input()
    if userSelection== "1":
        print("Enter a phrase to Encrypt")
        phrase = input()
        print("Enter the key phrase to use for encrypting:")
        myKey = input()

        keyArray = ['0']
        keyArray.remove('0')
        populatekeyarray(myKey, keyArray)


        result = ""
        x = 0
        for i in range(len(phrase)):
            char = phrase[i]

            if ((ord(char) >= 65 and ord(char)<= 90) or (ord(char) >= 97 and ord(char)<= 122)):
                keyChar = keyArray[x % len(myKey)]
                x=x+1
                if (keyChar.isupper()):
                    keyCharInt = ord(keyChar) - 65
                else:
                    keyCharInt = ord(keyChar) - 97
                if (char.isupper()):
                    result += chr((ord(char) + keyCharInt - 65) % 26 + 65)
                else:
                    result += chr((ord(char) + keyCharInt - 97) % 26 + 97)
            else:
                result += char
        print("The Encrypted ciphertext message is:" + result)
    if userSelection== "2":
        print("Please Enter a phrase to Decrypt")
        phrase = input()
        print("Enter the key number to use for Decrypting:")
        myKey = input()

        keyArray = ['0']
        keyArray.remove('0')
        populatekeyarray(myKey, keyArray)

        result = ""
        x = 0
        for i in range(len(phrase)):
            char = phrase[i]

            if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122)):
                keyChar = keyArray[x % len(myKey)]
                x = x + 1
                if (keyChar.isupper()):
                    keyCharInt = ord(keyChar) - 65
                else:
                    keyCharInt = ord(keyChar) - 97
                if (char.isupper()):
                    result += chr((ord(char) - keyCharInt - 65) % 26 + 65)
                else:
                    result += chr((ord(char) - keyCharInt - 97) % 26 + 97)
            else:
                result += char
        print("The Decrypted ciphertext message is:" + result)




def populatekeyarray(myKey,keyArray):
    for i in range(len(myKey)):
        keyArray.append(myKey[i])

if __name__ == '__main__':
    vCipher()


