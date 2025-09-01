
# Задачи по работе с файлами

# Задача 1
# Создай файл "example.txt" и запиши в него строку "Это пример записи в файл".
# Используй контекстный менеджер with.
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Это пример записи в файл")

# Задача 2
# Создай текстовый файл "data.txt", если его ещё нет.
# Открой файл в режиме добавления.
# Добавь в него строку "Новая строка данных\n".
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("Новая строка данных\n")

# Задача 3
# Открой файл "example.txt" для чтения.
# Считай содержимое файла и выведи его на экран.
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Задача 4
# Открой файл "data.txt" для чтения.
# Считай все строки файла и выведи каждую строку отдельно.
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Задача 5
# Создай новый файл "log.txt".
# Запиши в него три строки: "Первая запись", "Вторая запись", "Третья запись".
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("Первая запись\n")
    file.write("Вторая запись\n")
    file.write("Третья запись\n")

# Задача 6
# Создай файл "info.txt" и запиши в него строку "Информация о системе".
# Затем открой файл для чтения и выведи содержимое.
with open("info.txt", "w", encoding="utf-8") as file:
    file.write("Информация о системе")

with open("info.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Задача 7
# Создай файл "notes.txt" и запиши в него строку "Первая заметка".
# Затем открой файл в режиме 'a' и добавь строку "Вторая заметка".
# После этого прочитай файл и выведи его содержимое построчно.
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Первая заметка\n")
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Вторая заметка\n")
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Задача 8
# Открой файл "report.txt" в режиме добавления ("a").
# Добавь строку "Данные за понедельник".
with open("report.txt", "a", encoding="utf-8") as file:
    file.write("Данные за понедельник\n")
with open("report.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Задача 9
# Создай файл "log.txt" и запиши в него три строки:
# "Ошибка: файл не найден", "Ошибка: доступ запрещён", "Ошибка: неизвестная".
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("Ошибка: файл не найден\n")
    file.write("Ошибка: доступ запрещён\n")
    file.write("Ошибка: неизвестная\n")
with open("log.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Задача 10
# Удали файл "notes.txt".
import os
os.remove("notes.txt")