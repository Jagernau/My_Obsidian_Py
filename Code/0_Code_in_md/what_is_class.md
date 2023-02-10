```python
class My:
    x = 10
    def __init__(self):
        self.y = 777

    def get_value(self):
        return self.x

try:
    My.y = 666 
    # видимо при записи числа, y автоматически инициализируется
    print(My.y)
except BaseException:
    print("y ещё не появился")
finally:
    my = My()
    My.x = 20
    my.y = 26666
    print(f"{My}\n{my}\n{My.x}\n{my.y}")

```


