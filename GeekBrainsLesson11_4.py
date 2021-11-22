# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

class EquipmentStorage():
    def __init__(self, equipment_type, quantity):
        self.equipment_type = equipment_type
        self.quantity = quantity


class Printers(EquipmentStorage):
    def __init__(self, equipment_type, quantity, color):
        super().__init__(equipment_type, quantity)
        self.color = color


class Scanners(EquipmentStorage):
    def __init__(self, equipment_type, quantity, paper_format):
        super().__init__(equipment_type, quantity)
        self.paper_format = paper_format

class Xerox (EquipmentStorage):
    def __init__(self, equipment_type, quantity, sides):
        super().__init__(equipment_type, quantity)
        self.sides = sides


printers_group1 = Printers('HP printers', 4, 'multicolor')
scanners_group1 = Scanners("Cannon scanners", 2, 'A4')
xerox_group1 = Xerox('Xerox', 1, 2)

print(printers_group1)
print(scanners_group1)
print(xerox_group1)