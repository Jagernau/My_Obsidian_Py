```python
class My:
    value = 10

    def get_value(self):
        return self.value

MyClass = type("MyClass", (object, ), dict())
print(MyClass)
```
