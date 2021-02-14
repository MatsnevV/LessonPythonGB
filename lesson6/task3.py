"""
Реализовать базовый класс Worker (работник),в котором определить атрибуты: 
name, surname, position (должность),income (доход).

Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных 
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self):
        self.name = 'Иван'
        self.surname = 'Иванов'
        self.position = 'слесарь'
        self._income = dict()


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname, self.position)

    def get_total_income(self, wage=0, bonus=0):
        self._income = {"wage": wage, "bonus": bonus}
        print(f'Получает ЗП в размере: {self._income["wage"] + self._income["bonus"]}')


position = Position()
position.get_full_name()
position.get_total_income(10000, 5000)







