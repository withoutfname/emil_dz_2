
class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}, Тип: {self.toy_type}"


class ToyFactory:
    def create_toy(self, name, color, toy_type):
        self.purchase_materials()
        self.sew_toy()
        self.paint_toy(color)
        return Toy(name, color, toy_type)

    def purchase_materials(self):
        print("Закупка сырья для игрушки...")

    def sew_toy(self):
        print("Пошив игрушки...")

    def paint_toy(self, color):
        print(f"Окраска игрушки в цвет: {color}...")


factory = ToyFactory()
new_toy = factory.create_toy("Мишка", "Коричневый", "Животное")
print(new_toy)
