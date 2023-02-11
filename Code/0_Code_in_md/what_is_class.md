class My:
    x = 10  # просто атрибут класса

    def __init__(self):
        self.y = 777  # атр. экз. класса

    def get_value(self):
        return self.x


try:
    My.y = 666
    # видимо при записи числа, y автоматически инициализируется
    print(My.y)
except BaseException:
    print("y ещё не появился")
finally:
    my = My()  # Создали экземпляр класса
    My.x = 20
    my.y = 26666
    print(My)  # Класс это некий чертёж объекта,
    print(id(My))  # С сылкой для идентификации
    print(my)
    print(id(my))
    print(My.x)
    print(my.y)
