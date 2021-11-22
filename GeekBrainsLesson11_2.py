# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class ZeroDivisionException(Exception):
    def __init__(self, error_message):
        self.message = error_message


def division(a, b):
    try:
        if float(b) == 0:
            raise ZeroDivisionException('Error: factor is 0')
        c = float(a) / float(b)
    except ZeroDivisionException as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(round(c, 2))



print('function a/b')
a = input('input a: ')
b = input('input b: ')
division(a, b)
