
# Повторение всего материала по Python

# ===== Оглавление =====
# Переменные и типы данных: Задачи 1-3
# Строки: Задачи 1-2
# Списки: Задачи 1-2
# Условные операторы: Задачи 1-2
# Словари: Задача 1
# Циклы: Задачи 1-2
# Файлы: Задача 1
# Функции: Задача 1
# ООП ч.1: Задача 1
# ООП ч.2: Задача 1

# ===== Переменные и типы данных =====
# Задача 1
# Создай переменную age со значением 25.
# Создай переменную name со значением "Алексей".
# Выведи в консоль строку "Меня зовут {name}, мне {age} лет" с использованием f-строки.
age = 25
name = "Алексей"
print(f"Меня зовут {name}, мне {age} лет")

# Задача 2
# Создай число 25 и преобразуй его в строку, выведи тип полученной переменной.
value = 25
value_str = str(value)
print(type(value_str)) # Вывод <class 'str'>

# Задача 3
# Сравни числа 10 и 7 с помощью оператора >= и выведи результат.
print(10 >= 7) # Вывод True

# ===== Строки =====
# Задача 1
# Создай строку text со значением "Привет, мир!".
# Выведи первую букву строки и последние три буквы.
# Преобразуй строку в верхний регистр и выведи результат.
text = "Привет, мир!"
print(text[0])
print(text[-3:])
print(text.upper())

# Задача 2
# Создай строку с именем и возрастом, выведи через f-строку.
name = "Алексей"
age = 25
print(f"Меня зовут {name}, мне {age} лет")

# ===== Списки =====
# Задача 1
# Создай список fruits со значениями "яблоко", "банан", "вишня".
# Добавь элемент "апельсин" и удали первый элемент.
fruits = ["яблоко", "банан", "вишня"]
fruits.append("апельсин")
fruits.pop(0)
print(fruits)

# Задача 2
# Создай список numbers = [1,2,3], создай копию, измени первый элемент копии на 10.
my_list = [1, 2, 3]
copy_my_list = my_list.copy()
copy_my_list[0] = 10
print(my_list)
print(copy_my_list)

# ===== Условные операторы =====
# Задача 1
# Проверка числа: больше 0, равно 0, меньше 0.
number = 8
if number > 0:
    print("Положительное")
elif number == 0:
    print("Ноль")
else:
    print("Отрицательное")

# Задача 2
# Температура: выше 20, от 10 до 20, меньше 10.
temperature = 15
if temperature > 20:
    print("Тёпло")
elif 10 <= temperature <= 20:
    print("Прохладно")
else:
    print("Холодно")

# ===== Словари =====
# Задача 1
# Создай словарь person с вложенными словарями для name и address.
# Измени город на "Ставрополь", добавь postal_code, затем удали ключ city.
person = {
    "name": {"first_name": "Иван", "last_name": "Иванов"},
    "address": {"city": "Москва", "country": "Россия"}
}
person["address"]["city"] = "Ставрополь"
person["address"]["postal_code"] = "333777"
print(person["address"])
del person["address"]["city"]
print(person["address"])

# ===== Циклы =====
# Задача 1
# Вывод чисел от 1 до 20, пропуская числа кратные 4.
x = 1
while x <= 20:
    if x % 4 == 0:
        x += 1
        continue
    print(x)
    x += 1

# Задача 2
# С помощью цикла for выведи числа от 1 до 5.
for i in range(1,6):
    print(i)

# ===== Файлы =====
# Задача 1
# Создай файл fruits.txt и запиши фрукты, потом выведи строки, начинающиеся с 'а'.
with open("fruits.txt", "w", encoding="utf-8") as file:
    file.write("яблоко\nбанан\напельсин\n")

with open("fruits.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith("а"):
            print(line.strip())

# ===== Функции =====
# Задача 1
# Функция greet_user с параметрами user_role и user_name по умолчанию None.
def greet_user(user_role, user_name=None):
    if user_name:
        print(f"Привет, {user_name}! Ваша роль: {user_role}.")
    else:
        print(f"Привет, Гость! Ваша роль: {user_role}.")

greet_user("Администратор", "Алексей")
greet_user("Гость")

# ===== ООП ч.1 =====
# Задача 1
# Класс Student с атрибутами name и age, метод show_info.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(self.name, self.age)

student = Student("Алексей", 34)
student.show_info()

# ===== ООП ч.2 =====
# Задача 1
# Класс Animal и дочерний класс Dog с методами eat(), sleep(), bark().
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def eat(self):
        print(f"{self.name} ест")
    def sleep(self):
        print(f"{self.name} спит")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} лает")

my_dog = Dog("Шарик", "собака")
my_dog.eat()
my_dog.sleep()
my_dog.bark()
