class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала.")

    def stop(self):
        print(f"{self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.name} повернула на {direction}.")


class TownCar(Car):
    pass

class SportCar(Car):
    def boost(self):
        self.speed+=50
        print(f"{self.name} быстро ускорилась на 50 км/ч")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False, max_load=1000):
        super().__init__(speed, color, name, is_police)
        self.max_load = max_load

    def load(self, weight):
        print(f"{self.name} загружена грузом массой {weight} кг.")








