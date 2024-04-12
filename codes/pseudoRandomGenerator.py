def setParams():
    try:
        a = int(input('Введите значение а:'))
        c = int(input('Введите значение c:'))
        m = int(input('Введите значение m:'))
        seed = int(input('Введите значение seed:'))
        n = int(input('Введите значение n:'))
        return a , c , m , seed , n
    except ValueError as e:
        print('Неправильно введены данные')

def generator(a , c , m , seed , n):
    X = seed
    random_numbers = []

    for _ in range(n):
        X = (a * X + c) % m 
        random_numbers.append(X)
    return random_numbers

def main():
    a , c , m , seed , n = setParams()
    result = generator(a , c , m , seed , n)
    print('Результат: '  , result)

if __name__ == '__main__':
    main()


    