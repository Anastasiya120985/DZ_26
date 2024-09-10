# Задание 1
# Создайте реализацию паттерна Builder. Протестируйте работу созданного класса.
class Phone:
    def __init__(self):
        self.os = None
        self.camera = None
        self.battery = None
        self.screen = None


class PhoneBuilder:
    def __init__(self):
        self.phone = Phone()

    def set_os(self, os):
        self.phone.os = os
        return self

    def set_camera(self, camera):
        self.phone.camera = camera
        return self

    def set_battery(self, battery):
        self.phone.battery = battery
        return self

    def set_screen(self, screen):
        self.phone.screen = screen
        return self


builder = PhoneBuilder()
phone = builder.set_os("Android").set_camera("12 MP").set_battery("3500 mAh").set_screen("6.2 inches").get_phone()

# Задание 2
# Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три
# вида пасты. Классы различной пасты должны иметь следующие методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.


# Задание 3
# Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.
import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj


class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Camry"
        self.year = 2020

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"


prototype = Prototype()
car = Car()
prototype.register_object("car", car)
car_clone = prototype.clone("car", year=2021)
print(car)
print(car_clone)
