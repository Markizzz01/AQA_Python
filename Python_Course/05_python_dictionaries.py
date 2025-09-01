
# Задачи по словарям

# Задача 1
# Создай словарь person с ключами "name" и "age", значениями "Алексей" и 25
# Выведи этот словарь на экран
person = {
    "name": "Алексей",
    "age": 25
}
print(person)

# Задача 2
# Создай пустой словарь book. Добавь ключ "title" со значением "Python 101"
# Выведи обновлённый словарь
book = {}
book["title"] = "Python 101"
print(book)

# Задача 3
# Создай словарь user с ключами "login" и "password", значениями "admin" и "1234"
# Выведи значение по ключу "login"
user = {
    "login": "admin",
    "password": "1234"
}
print(user["login"])

# Задача 4
# Удали из словаря user ключ "password"
# Выведи обновлённый словарь
del user["password"]
print(user)

# Задача 5
# Создай словарь product с ключами "name" и "price", значениями "яблоко" и 50
# Обнови значение ключа "price" на 60
# Выведи словарь
product = {
    "name": "яблоко",
    "price": 50
}
product["price"] = 60
print(product)

# Задача 6
# Создай словарь car с ключами "brand", "model", "year", значениями "Toyota", "Corolla", 2020
# Выведи все ключи словаря
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}
print(car.keys())

# Задача 7
# Создай словарь student с ключами "name", "grade", "age", значениями "Иван", 5, 17
# Выведи все значения словаря
student = {
    "name": "Иван",
    "grade": 5,
    "age": 17
}
print(student.values())

# Задача 8
# Создай словарь city с ключами "name" и "population", значениями "Москва" и 12_500_000
# Проверь, есть ли в словаре ключ "country"
city = {
    "name": "Москва",
    "population": 12_500_000
}
print("country" in city)

# Задача 9
# Создай словарь employee с ключами "name", "position", "salary", значениями "Анна", "менеджер", 50000
# Проверь, есть ли в словаре значение "менеджер"
employee = {
    "name": "Анна",
    "position": "менеджер",
    "salary": 50000
}
print("менеджер" in employee.values())

# Задача 10
# Создай словарь phone с ключами "brand", "model", "price", значениями "Samsung", "Galaxy S21", 70000
# Проверь, есть ли ключ "model" и значение 60000, выведи результаты
phone = {
    "brand": "Samsung",
    "model": "Galaxy S21",
    "price": 70000
}
print("model" in phone)
print(60000 in phone.values())

# Задача 11
# Создай словарь inventory с ключами "apples", "oranges", "bananas", значениями 10, 20, 15
# Удали ключ "oranges" и выведи обновлённый словарь
inventory = {
    "apples": 10,
    "oranges": 20,
    "bananas": 15
}
del inventory["oranges"]
print(inventory)

# Задача 12
# Создай словарь animal с ключами "type", "name", "age", значениями "кошка", "Муся", 3
# Выведи все пары ключ-значение
animal = {
    "type": "кошка",
    "name": "Муся",
    "age": 3
}
print(animal.items())

# Задача 13
# Создай словарь movie с ключами "title", "year", "genre", значениями "Inception", 2010, "sci-fi"
# Обнови жанр на "fantasy" и выведи словарь
movie = {
    "title": "Inception",
    "year": 2010,
    "genre": "sci-fi"
}
movie["genre"] = "fantasy"
print(movie)

# Задача 14
# Создай словарь user с ключами "name" и "email", значениями "Олег", "oleg@example.com"
# Проверь, есть ли значение "Олег" в словаре
user = {
    "name": "Олег",
    "email": "oleg@example.com"
}
print("Олег" in user.values())

# Задача 15
# Создай словарь profile с ключами "username", "email", "active", значениями "markizzz", "markizzz@example.com", True
# Если ключ "active" есть в словаре — удали его
profile = {
    "username": "markizzz",
    "email": "markizzz@example.com",
    "active": True
}
if "active" in profile:
    del profile["active"]
print(profile)