def getWord():
    word = input('Введите слово, которое хотите зашифровать: ')
    if len(word) > 0:
        ascii_word = [ord(char) for char in word] 
    length =  len(word) 
    return ascii_word , length

def getKey():
    ascii_word , length = getWord()
    key = str(input(f'Введите ключ для шифрования, длина которго равна {length}: '))
    if len(key) != len(ascii_word):
        print('Введенный ключ не подходит из-за длины.\nПопробуйте снова.')
        getKey()
    else:
        ascii_key = [ord(char) for char in key]
        return ascii_word , ascii_key
    
def encryptText():
    ascii_word , ascii_key = getKey()
    encrypt_text = []
    for i in range(len(ascii_word)):
        encrypt_text.append(ascii_word[i] ^ ascii_key[i])
    print(encrypt_text)
    return encrypt_text , ascii_key

def decryptText():
    ecrypt_text , ascii_key = encryptText()
    decrypt_text = []
    for i in range(len(ascii_key)):
        decrypt_text.append(chr((ascii_key[i] ^ ecrypt_text[i])))
    print(decrypt_text)
    return decrypt_text

def main():
    decryptText()

if __name__ == "__main__":
    main()
