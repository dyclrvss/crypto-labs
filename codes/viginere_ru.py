def vCipher():
    print("Введите 1 для кодирования сообщения")
    print("Введите 2 для декодирования сообщения")
    print("Введите 3 для выхода")
    userSelection = input()
    if userSelection == "1":
        print("Пожалуйста, введите фразу для шифрования:")
        phrase = input()
        print("Введите ключевую фразу для шифрования:")
        myKey = input()

        keyArray = []
        populatekeyarray(myKey, keyArray)

        result = ""
        x = 0
        for i in range(len(phrase)):
            char = phrase[i]

            if ord('а') <= ord(char) <= ord('я') or ord('А') <= ord(char) <= ord('Я'):
                keyChar = keyArray[x % len(myKey)]
                x += 1
                if keyChar.isupper():
                    keyCharInt = ord(keyChar) - ord('А')
                else:
                    keyCharInt = ord(keyChar) - ord('а')
                if char.isupper():
                    result += chr((ord(char) + keyCharInt - ord('А')) % 32 + ord('А'))
                else:
                    result += chr((ord(char) + keyCharInt - ord('а')) % 32 + ord('а'))
            else:
                result += char
        print("Зашифрованное сообщение: " + result)
    elif userSelection == "2":
        print("Пожалуйста, введите фразу для декодирования:")
        phrase = input()
        print("Введите ключевую фразу для декодирования:")
        myKey = input()

        keyArray = []
        populatekeyarray(myKey, keyArray)

        result = ""
        x = 0
        for i in range(len(phrase)):
            char = phrase[i]

            if ord('а') <= ord(char) <= ord('я') or ord('А') <= ord(char) <= ord('Я'):
                keyChar = keyArray[x % len(myKey)]
                x += 1
                if keyChar.isupper():
                    keyCharInt = ord(keyChar) - ord('А')
                else:
                    keyCharInt = ord(keyChar) - ord('а')
                if char.isupper():
                    result += chr((ord(char) - keyCharInt - ord('А')) % 32 + ord('А'))
                else:
                    result += chr((ord(char) - keyCharInt - ord('а')) % 32 + ord('а'))
            else:
                result += char
        print("Декодированное сообщение: " + result)


def populatekeyarray(myKey, keyArray):
    for i in range(len(myKey)):
        keyArray.append(myKey[i])


if __name__ == '__main__':
    vCipher()
