# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def data_extractor(cls, data):
        try:
            return tuple(map(int, data.split('-')))
        except Exception as e:
            return f'{data}  -  {e}'

    @staticmethod
    def data_validation(obj):
        try:
            # извлекаем день месяц год из строки
            day = Data.data_extractor(obj)[0]
            month = Data.data_extractor(obj)[1]
            year = Data.data_extractor(obj)[2]
            # определяем месяцы с 31 днем в году
            big_month = (1, 3, 5, 7, 8, 10, 12)
            # определяем месяцы с 30 днеми в году
            small_month = (2, 4, 6, 9, 11)
            # проверяеем что дады авляюся int
            if not isinstance(day, int):
                return print('wrong data format')
            if not isinstance(month, int):
                return print('wrong data format')
            if not isinstance(year, int):
                return print('wrong data format')

            # есяцев должно быть от 1 до 12
            if 12 < month or month < 1:
                return print('month should be from range 1 - 12')
            # проверяем дни в месяцах в которых 31 день
            if big_month.count(month) > 0 and (1 > day or day > 31):
                return print(f"{day} is incorrect day value for month {month}")
            # проверяем дни в месяцах в которых 30 деней
            if small_month.count(month) > 0 and (1 > day or day > 30):
                return print(f"{day} is incorrect day value for month {month}")
            # проверяем дни в феврале в высокосный год
            if month == 2 and year % 4 == 0 and (1 > day or day > 29):
                return print(f"{day} is incorrect day value for month {month} and year {year}")
            # проверяем дни в феврале 
            if month == 2 and year % 4 != 0 and (1 > day or day > 28):
                return print(f"{day} is incorrect day value for month {month} and year {year}")
            return print('data inputted correctly')
        except Exception as e:
            print(e)


check_dates = ('29-02-1991', '32-01-2020', '31-04-2017', '31-05-2017', '12-13-2021', '-12-13--2014', '12-56.6-25', '0,5-78-2')
for date in check_dates:
    print(Data.data_extractor(date))
    test_data = Data(date)
    test_data.data_validation(test_data.data)
