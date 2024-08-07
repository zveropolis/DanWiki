Позиционные аргументы функции - это аргументы, которые передаются без явного указания названия в определенном порядке.
Символ `/`, передаваемый в качестве аргумента функции явно задает отсутствие именованных аргументов:
```python
def my_function(x, /):  
  ...

# my_function(x = 3) # > Exception
```
Именованные аргументы - аргументы с явно заданным названием (или значением по умолчанию).
Тогда как символ `*`, напротив, задает отсутствие позиционных:
```python
def my_function(*, x):  
  ...

# my_function(3) # > Exception
```
Вы можете объединить два типа аргументов в одной функции.
Любой аргумент _перед_ `/ ,` является только позиционным, а любой аргумент _после_ `*,` - только ключевым словом.
```python
def my_function(a, b, /, *, c, d):  
  print(a + b + c + d)  
  
my_function(5, 6, c = 7, d = 8)
```
Собрать все входящие позиционные и/или именованные аргументы:
```python
def function(*args, **kwargs):
	...
```
`args` - список, содержащий все аргументы, переданные без указания названия.
`kwargs` - словарь, имеющий структуру **_название_** : **_значение_**.

> [!important]
> В программировании функция, которая возвращает значение `True` или `False`, называется **предикатом**.

# match
```python
from http import HTTPStatus
import random

http_status = random.choice(list(HTTPStatus))

match http_status:
    case 200 | 201 | 204 as status:
        # 👆 Using "as status" extracts its value
        print(f"Everything is good! {status = }") # 👈 Now status can be used inside handler

    case 400 | 404 as status:
        print(f"You did something wrong! {status = }")

    case 500 as status:
        print(f"Oops... Is the server down!? {status = }")

    case _ as status:
        print(f"No clue what to do with {status = }!")
```

```python
match settings.param_name:
    case str():
        logger.info('is a str')
    case _:
        logger.info('not str')
```