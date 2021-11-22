# Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

# class for error raising with custom text if data was inputted incorrectly
class MyError(Exception):
    def __init__(self, message):
        self.message = message


class EquipmentStorage:

    def __init__(self, equipment_type, quantity):
        self.equipment_type = equipment_type
        self.quantity = quantity
        self.location = {"Storage": quantity}

    def to_storage(self):
        # new location of equipment
        to_place = input(
            f"Please enter where {self.equipment_type} should be put. For example Office_room1, meeting_room1 etc.\n").title()
        # from where equipment should be replaced. inputting in a loop till correct location
        while True:
            from_place = input(
                f"Please enter from where {self.equipment_type} should be replace. Available locations: {list(self.location.keys())}.\n").title()
            if self.location.__contains__(from_place.title()):
                break
            else:
                print(f'No {self.equipment_type} at {from_place.title()} now. Please select another location')

        # quantity of equipment to be replaced. inputting in a loop till correct quantity
        while True:
            try:
                quantity = int(input(
                    f'Please enter quatity of {self.equipment_type} to replace. Currently availible: {self.location.get(from_place)}.\n'))
                if quantity < 1:
                    raise MyError("quantity should be more than 0")
                elif self.location[from_place.title()] < quantity:
                    raise MyError(
                        f"It is not possible to move {quantity} {self.equipment_type} to {to_place.title()}.\n"
                        f"Current available numbers of {self.equipment_type} at {from_place.title()} is {self.location.get(from_place.title())}.\n")
            except MyError as e:
                print(e)
            except Exception as e:
                print(e)
            else:
                break
        # changing quantity in items
        self.location[to_place.title()] = quantity
        self.location[from_place.title()] -= quantity
        print(f'{quantity} {self.equipment_type} were moved to {to_place.title()}. \nCurrent status is: {self.location}\n')


class Printers(EquipmentStorage):
    def __init__(self, equipment_type, quantity, color):
        super().__init__(equipment_type, quantity)
        self.color = color


class Scanners(EquipmentStorage):
    def __init__(self, equipment_type, quantity, paper_format):
        super().__init__(equipment_type, quantity)
        self.paper_format = paper_format


class Xerox(EquipmentStorage):
    def __init__(self, equipment_type, quantity, sides):
        super().__init__(equipment_type, quantity)
        self.sides = sides


# creating class items
printers_group1 = Printers('HP printer', 4, 'multicolor')
scanners_group1 = Scanners("Cannon scanner", 4, 'A4')
xerox_group1 = Xerox('Xerox', 4, 2)

print(
    f'\n*****Current status*****\n{printers_group1.equipment_type}: {printers_group1.location}\n{scanners_group1.equipment_type}: {scanners_group1.location}\n{xerox_group1.equipment_type}: {xerox_group1.location}\n')

# user's interface initialisation :)
while True:
    equipment_type = input(
        f'Enter equipment you want to move (available equipment: {printers_group1.equipment_type}, {scanners_group1.equipment_type}, {xerox_group1.equipment_type}): ').lower()
    if equipment_type == printers_group1.equipment_type.lower():
        printers_group1.to_storage()
    elif equipment_type == scanners_group1.equipment_type.lower():
        scanners_group1.to_storage()
    elif equipment_type == xerox_group1.equipment_type.lower():
        xerox_group1.to_storage()
    else:
        print(f'There is no {equipment_type}.')
