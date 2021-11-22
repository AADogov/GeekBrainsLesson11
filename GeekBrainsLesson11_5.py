# Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

class EquipmentStorage:

    def __init__(self, equipment_type, quantity):
        self.equipment_type = equipment_type
        self.quantity = quantity
        self.location = {"Storage": quantity}

    def to_storage(self, from_place, to_place, quantity):
        if self.location.__contains__(from_place.title()):
            if self.location[from_place.title()] >= quantity:
                self.location[to_place.title()] = quantity
                self.location[from_place.title()] -= quantity
                print(f'{quantity} {self.equipment_type} were moved to {to_place.title()}. \nCurrent status is: {self.location}\n')
            else:
                print(f"It is not possible to move {quantity} {self.equipment_type} to {to_place.title()}.\n"
                      f"Current available {self.equipment_type} at {from_place.title()} is {self.location.get(from_place.title())}.\n")
        else:
            print(f'No {self.equipment_type} at {to_place.title()} now. Please select another location')


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
printers_group1 = Printers('HP printer(s)', 4, 'multicolor')
scanners_group1 = Scanners("Cannon scanner(s)", 4, 'A4')
xerox_group1 = Xerox('Xerox(es)', 4, 2)
# moving printers to office
printers_group1.to_storage("storage", "office_room1", 2)
printers_group1.to_storage("storage", "office_room2", 3)
printers_group1.to_storage("storage", "office_room2", 2)
printers_group1.to_storage("storage", "office_room3", 1)
