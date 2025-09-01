
# Задачи по функциям

# Задача 1
# Создай функцию greet, которая выводит "Привет, мир!".
def greet():
    print("Привет, мир!")

greet() # Вывод Привет, мир!

# Задача 2
# Создай функцию say_hello, которая выводит "Привет!".
def say_hello():
    print("Привет!")

say_hello() # Вывод Привет!

# Задача 3
# Создай функцию greet, которая принимает имя и выводит "Привет, <имя>!".
def greet(name):
    print(f"Привет, {name}!")

greet("Алексей") # Вывод Привет, Алексей!

# Задача 4
# Создай функцию multiply, которая принимает два числа и возвращает их произведение.
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result) # Вывод 20

# Задача 5
# Создай функцию greet_person с аргументами name и age=18.
# Выводит "Привет, <name>! Тебе <age> лет."
def greet_person(name, age=18):
    print(f"Привет, {name}! Тебе {age} лет.")

greet_person("Эдик") # Вывод Привет, Эдик! Тебе 18 лет.

# Задача 6
# Создай функцию square, которая возвращает квадрат числа.
def square(num):
    return num ** 2

print(square(6)) # Вывод 36

# Задача 7
# Создай декоратор log_message, который перед выполнением функции выводит "Выполняется функция..."
def log_message(func):
    def wrapper():
        print("Выполняется функция...")
        func()
    return wrapper

@log_message
def hello():
    print("Привет!")

hello() # Вывод Выполняется функция... Привет!

# Задача 8
# Создай функцию concatenate, которая принимает две строки и возвращает их объединение.
def concatenate(a, b):
    return a + b

print(concatenate("Привет, ", "мир!")) # Вывод Привет, мир!

# Задача 9
# Напиши функцию is_positive, которая возвращает True, если число > 0, иначе False.
def is_positive(num):
    return num > 0

print(is_positive(-5)) # Вывод False

# Задача 10
# Напиши функцию is_negative, которая возвращает True, если число < 0, иначе False.
def is_negative(num):
    return num < 0

print(is_negative(12)) # Вывод False

# Задача 11
# Напиши функцию greet_user с аргументами name и language="ru".
# Если language=="ru", вывод "Привет, <name>!", иначе "Hello, <name>!"
def greet_user(name, language="ru"):
    if language == "ru":
        print(f"Привет, {name}!")
    else:
        print(f"Hello, {name}!")

greet_user("Лена") # Вывод Привет, Лена!
greet_user("Лена", "en") # Вывод Hello, Лена!

# Задача 12
# Напиши функцию get_square, которая возвращает квадрат числа.
def get_square(num):
    return num ** 2

print(get_square(7)) # Вывод 49

# Задача 13
# Напиши функцию get_power, которая принимает число и степень (по умолчанию 2)
def get_power(num, power=2):
    return num ** power

print(get_power(5, 3)) # Вывод 125
print(get_power(4))    # Вывод 16

# Задача 14
# Создай функцию is_divisible, которая возвращает True, если num делится на divisor без остатка
def is_divisible(num, divisor):
    return num % divisor == 0

print(is_divisible(10, 5)) # Вывод True

# Задача 15
# Создай декоратор uppercase_decorator, который преобразует строку в верхний регистр
def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "привет"

print(say_hello()) # Вывод ПРИВЕТ

# Задача 16
# Создай функцию greet_person, которая возвращает строку "Привет, <name>! Тебе <age> лет."
def greet_person(name, age):
    return f"Привет, {name}! Тебе {age} лет."

print(greet_person("Иван", 35)) # Вывод Привет, Иван! Тебе 35 лет.

