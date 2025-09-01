
# Задачи по ООП часть 2 (Наследование)

# Задача 1
# Создай базовый класс Animal с методом speak, который выводит "Животное издаёт звук".
# Создай подкласс Dog, который наследует Animal и переопредели метод speak так, чтобы выводил "Собака лает".
class Animal:
    def speak(self):
        print("Животное издаёт звук")

class Dog(Animal):
    def speak(self):
        print("Собака лает")

dog = Dog()
dog.speak() # Вывод Собака лает

# Задача 2
# Создай родительский класс Vehicle с методом move, который выводит "Транспорт едет".
# Создай дочерний класс Car, который наследует Vehicle и переопредели метод move, чтобы выводил "Машина едет быстро".
class Vehicle:
    def move(self):
        print("Транспорт едет")

class Car(Vehicle):
    def move(self):
        print("Машина едет быстро")

car = Car()
car.move() # Вывод Машина едет быстро

# Задача 3
# Создай класс Car с атрибутами make и model.
# Метод display_info выводит "<марка> <модель>".
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"{self.make} {self.model}")

car = Car("VW", "Passat")
car.display_info() # Вывод VW Passat

# Задача 4
# Создай родительский класс Animal с методом sound(), который выводит "Животное издаёт звук".
# Создай дочерний класс Cat, который переопределяет метод sound(), чтобы выводил "Кошка мяукает".
class Animal:
    def sound(self):
        print("Животное издает звук")

class Cat(Animal):
    def sound(self):
        print("Кошка мяукает")

cat = Cat()
cat.sound() # Вывод Кошка мяукает

# Задача 5
# Создай родительский класс Vehicle с методом move(), который выводит "Транспорт движется".
# Создай дочерний класс Bicycle, который переопределяет метод move(), чтобы выводил "Велосипед едет".
class Vehicle:
    def move(self):
        print("Транспорт движется")

class Bicycle(Vehicle):
    def move(self):
        print("Велосипед едет")

bike = Bicycle()
bike.move() # Вывод Велосипед едет

# Задача 6
# Создай родительский класс Person с атрибутом name и методом greet().
# Создай дочерний класс Student, который наследует Person и добавляет атрибут course.
# Переопредели метод greet(), чтобы выводил "Привет, меня зовут {name}, я учусь на курсе {course}".
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привет, меня зовут {self.name}")

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def greet(self):
        print(f"Привет, меня зовут {self.name}, я учусь на курсе {self.course}")

student = Student("Алексей", "Python")
student.greet() # Вывод Привет, меня зовут Алексей, я учусь на курсе Python

# Задача 7
# Создай родительский класс Vehicle с атрибутом brand и методом drive().
# Создай дочерний класс Car, который добавляет атрибут model и переопределяет метод drive().
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"Транспорт {self.brand} едет")

class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Машина {self.brand} {self.model} едет быстро")

car = Car("Skoda","Superb")
car.drive() # Вывод Машина Skoda Superb едет быстро

# Задача 8
# Создай родительский класс Animal с атрибутом name и методом speak().
# Создай дочерний класс Dog с атрибутом breed.
# Переопредели метод speak(), чтобы выводил "Собака породы {breed} по кличке {name} лает".
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Животное {self.name} издаёт звук.")

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print(f"Собака породы {self.breed} по кличке {self.name} лает")

dog = Dog("Милка", "французский бульдог")
dog.speak() # Вывод Собака породы французский бульдог по кличке Милка лает

# Задача 9
# Создай родительский класс Appliance с атрибутом brand и методом turn_on().
# Создай дочерний класс WashingMachine с атрибутом load_capacity.
# Переопредели метод turn_on().
class Appliance:
    def __init__(self, brand):
        self.brand = brand

    def turn_on(self):
        print(f"Прибор {self.brand} включен")

class WashingMachine(Appliance):
    def __init__(self, brand, load_capacity):
        self.brand = brand
        self.load_capacity = load_capacity

    def turn_on(self):
        print(f"Стиральная машина {self.brand} с загрузкой {self.load_capacity} кг включена")

wash = WashingMachine("LG",3)
wash.turn_on() # Вывод Стиральная машина LG с загрузкой 3 кг включена

# Задача 10
# Создай родительский класс Device с атрибутом brand и методом power_on().
# Создай дочерний класс Smartphone с атрибутом model.
# Переопредели метод power_on().
class Device:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"Устройство {self.brand} включено")

class Smartphone(Device):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"Смартфон {self.brand} {self.model} включен и готов к работе")

phone = Smartphone("iPhone", 16)
phone.power_on() # Вывод Смартфон iPhone 16 включен и готов к работе