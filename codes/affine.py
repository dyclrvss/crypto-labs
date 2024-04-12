import math

def affine(name = None, surname = None):

    name = input("Введите имя: ", )
    surname = input('Введите фамилию: ', )
    mod = int(input('Введите количество букв в алфавите: ', ))
    A = int(input('Введите значение A: ', ))

    if math.gcd(A, mod) != 1:
        print ('Неправильное условие')
        affine()
    else:
        B = int(input('Введите значение В: ' ))
        cipher_name = ''
        cipher_surname = ''
        
        for char in name:
            x = ord(char.lower()) - ord('а')
            y = (A * x + B) % mod
            cipher = chr(y + ord('а'))
            cipher_name += cipher

        for char in surname:
            x1 = ord(char.lower()) - ord('а')
            y1 = (A * x1 + B) % mod
            cipher1 = chr(y1 + ord('а'))
            cipher_surname += cipher1
        
        print('Зашифрованный текст:', cipher_name, cipher_surname)

        a = pow(A, -1, mod)

        decipher_name = ''
        decipher_surname = ''
        for char in cipher_name:
            x2 = ord(char.lower()) - ord('а')
            y2 = a * (x2 - B) % mod
            decipher = chr(y2 + ord('а'))
            decipher_name += decipher

        for char in cipher_surname:
            x3 = ord(char.lower()) - ord('а')
            y3 = a * (x3 - B) % mod
            decipher1 = chr(y3 + ord('а'))
            decipher_surname += decipher1

        print('Расшифрованный текст:', decipher_name, decipher_surname)

if __name__ == '__main__':
    affine()
