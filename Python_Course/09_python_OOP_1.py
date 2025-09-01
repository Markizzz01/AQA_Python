
# Задачи по ООП часть 1

# Задача 1
# Создай класс Student с атрибутами name и age.
# Метод show_info выводит имя и возраст.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)

student = Student("Алексей", 34)
student.show_info() # Вывод Алексей 34

# Задача 2
# Создай класс Dog с методом bark, который выводит "Гав!".
class Dog:
    def bark(self):
        print("Гав!")

my_dog = Dog()
my_dog.bark() # Вывод Гав!

# Задача 3
# Создай класс Cat с атрибутом name.
# Метод meow выводит "Мяу! Меня зовут <name>".
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"Мяу! Меня зовут {self.name}")

cat1 = Cat("Мурка")
cat1.meow() # Вывод Мяу! Меня зовут Мурка

# Задача 4
# Создай класс Person с атрибутами name и age.
# Метод introduce выводит "Меня зовут <name>, мне <age> лет."
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет.")

person1 = Person("Оля", 28)
person1.introduce() # Вывод Меня зовут Оля, мне 28 лет.

# Задача 5
# Создай класс Rectangle с атрибутами width и height.
# Метод area возвращает площадь.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(rect.area()) # Вывод 50

# Задача 6
# Создай класс BankAccount с атрибутами owner и balance=0.
# Методы: deposit(amount), withdraw(amount), display_balance()
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств")

    def display_balance(self):
        print(f"Баланс владельца {self.owner}: {self.balance}")

account = BankAccount("Иван", 100)
account.deposit(50)
account.withdraw(30)
account.display_balance() # Вывод Баланс владельца Иван: 120
account.withdraw(150)     # Вывод Недостаточно средств
account.display_balance() # Вывод Баланс владельца Иван: 120

# Задача 7
# Создай класс Book с атрибутами title и author.
# Метод info выводит "Книга '<title>' написана автором <author>."
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Книга '{self.title}' написана автором {self.author}")

book_1 = Book("Пророк", "Пушкин")
book_1.info() # Вывод Книга 'Пророк' написана автором Пушкин

# Задача 8
# Создай класс Circle с атрибутом radius.
# Метод area возвращает площадь круга.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

my_circle = Circle(5)
print(my_circle.area()) # Вывод 78.5

# Задача 9
# Создай класс Animal с атрибутами species и name.
# Метод speak выводит "<name> — это <species>, и он издаёт звук!"
class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def speak(self):
        print(f"{self.name} — это {self.species}, и он издаёт звук!")

animal = Animal("Жизнь", "Драйв")
animal.speak() # Вывод Жизнь — это Драйв, и он издаёт звук!

# Задача 10
# Создай класс Book с атрибутами title и author.
# Метод show_info выводит "<title>" написана автором <author>.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"{self.title} написана автором {self.author}.")

book = Book("Война и мир","Толстой")
book.show_info() # Вывод Война и мир написана автором Толстой.

