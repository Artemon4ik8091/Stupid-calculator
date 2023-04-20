restart = 1
print("Идиотский калькулятор")
while(restart == 1):   
    work = input("Введите желаемую операцию (+ - / * для выхода напишите exit): ")
    с = 0
    if work == "+":
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = a + b
        print("Ответ: " + str(c))
    if work == "-":
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = a - b
        print("Ответ: " + str(c))
    if work == "*":
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = a * b
        print("Ответ: " + str(c))
    if work == "/":
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = a / b
        print("Ответ: " + str(c))
    if work == "exit":
        print("Завершение работы...")
        restart = 0