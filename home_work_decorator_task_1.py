# Доработать декоратор logger в коде ниже.
# Должен получиться декоратор, который записывает в файл 'main.log' дату
# и время вызова функции, имя функции, аргументы, с которыми вызвалась,
# возвращаемое значение. Функция test_1 в коде ниже также должна отработать без ошибок.

import os
import datetime

def logger(old_function):

    def new_function(*args, **kwargs):
        current = os.getcwd()  # текущая директория, без привязки к ОС
        folder_name = "folder"
        file_name = 'main.log'
        full_path = os.path.join(current, folder_name, file_name)  # полный путь

        with open(full_path, "a", encoding='utf-8') as file:
            file.write(f"\nдата вызова функции: {datetime.datetime.today().strftime('%d:%m:%Y время: %H:%M:%S')}\n"
                        f"наименование функции {old_function.__name__}\n"
                        f"аргументы функции: {args=}, {kwargs=}\n")

            value = old_function(*args, **kwargs)

            file.write(f"результат выполнения функции равен {value}\n")
            return value
    return new_function

def test_1():

    path = 'folder/main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()