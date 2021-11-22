# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку
# методов сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса
# (комплексные числа), выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного
# результата.

class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} + {self.y}i'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return ComplexNumber(x, y)

    def __mul__(self, other):
        x = self.x * other.x - self.y * other.y
        y = self.x * other.y + other.x * self.y
        return ComplexNumber(x, y)


complex_1 = ComplexNumber(2, 4)
complex_2 = ComplexNumber(4, 8)
print('***** complex numbers *****')
print(complex_2)
print(complex_1)
print('***** adding *****')
print(complex_1 + complex_2)
print('***** multiplying *****')
print(complex_1 * complex_2)
