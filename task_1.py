# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


import os

def split_path(path):
    file_path, file_name = os.path.split(path)
    file_name, file_extension = os.path.splitext(file_name)
    return file_path, file_name, file_extension

path = '/home/user/documents/example.txt'
result = split_path(path)
print(result)