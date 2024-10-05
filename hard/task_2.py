class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}, Тип: {self.toy_type}"


class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, "Животное")


class CartoonCharacterToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, "Персонаж мультфильма")


class ToyFactory:
    def create_toy(self, name, color, toy_type):
        self.purchase_materials()
        self.sew_toy()
        self.paint_toy(color)

        if toy_type == "Животное":
            return AnimalToy(name, color)
        elif toy_type == "Персонаж мультфильма":
            return CartoonCharacterToy(name, color)
        else:
            print("Неизвестный тип игрушки!")
            return None

    def purchase_materials(self):
        print("Закупка сырья для игрушки...")

    def sew_toy(self):
        print("Пошив игрушки...")

    def paint_toy(self, color):
        print(f"Окраска игрушки в цвет: {color}...")


factory = ToyFactory()


bear = factory.create_toy("Мишка", "Коричневый", "Животное")
print(bear)


mickey = factory.create_toy("Микки Маус", "Черный", "Персонаж мультфильма")
print(mickey)
