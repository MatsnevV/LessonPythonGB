"""
Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка). 
 Метод выводит сообщение “Запуск отрисовки.” 
 Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
 В каждом из классов реализовать переопределение метода draw. 
 Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self):
        self.title = ' '

    def draw(self):
        return "Запуск отрисовки." + self.title


class Pencil(Stationery):

    def draw(self):
        self.title = 'карандаш'
        return "Запуск отрисовки." + self.title


class Pen(Stationery):
    def draw(self):
        self.title = "ручка"
        return "Запуск отрисовки." + self.title


class Handle(Stationery):
    def draw(self):
        self.title = 'маркер'
        return "Запуск отрисовки." + self.title


handle = Handle()
pen = Pen()
pencil = Pencil()

print(pen.draw())
print(pencil.draw())
print(handle.draw())
