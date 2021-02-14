"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность
первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time


class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']
        self.__sleepers = [7, 2, 15]

    def running(self):
        for i, j in enumerate(self.__color):
            print(j)
            time.sleep(self.__sleepers[i])


trafficLight = TrafficLight()
trafficLight.running()













