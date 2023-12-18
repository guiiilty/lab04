# Лабораторная работа №4
## Сложность: Rare
### Задание
1. Скачайте архив и распакуйте его в свой репозиторий. В нём 11 заданий, которые вам нужно выполнить.
2. Оформите отчёт в README.md. По каждому из заданий - описание задачи, скриншот работы программы.

### Ход работы
### Задание 00
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distance = {}

Moscow_London = ((sites['Moscow'][0] - sites['London'][0]) ** 2 + (sites['Moscow'][1] - sites['London'][1]) ** 2) ** 0.5
London_Paris = ((sites['London'][0] - sites['Paris'][0]) ** 2 + (sites['London'][1] - sites['Paris'][1]) ** 2) ** 0.5
Paris_Moscow = ((sites['Paris'][0] - sites['Moscow'][0]) ** 2 + (sites['Paris'][1] - sites['Moscow'][1]) ** 2) ** 0.5
distance['Moscow-London'] = round(Moscow_London, 1)
distance['London-Paris'] = round(London_Paris, 1)
distance['Paris-Moscow'] = round(Paris_Moscow, 1)

print(distance)
```
Скриншот работы программы 0.

![Alt text](Term_1.png)

### Задание 01
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r = 42
pi = 3.1415926
s = pi * r**2
print(round(s, 4))

point_1 = (23, 34)
dist_1 = ((point_1[0] ** 2 + point_1[1] ** 2) ** 0.5)
if dist_1 < r:
    print(True)
else:
    print(False)

point_2 = (30, 30)
dist_2 = ((point_2[0] ** 2 + point_2[1] ** 2) ** 0.5)
if dist_2 < r:
    print(True)
else:
    print(False)
```
Скриншот работы программы 1.

![Alt text](Term_0.png)

### Задание 02
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Пример без скобок
result = 1 * 2 + 3 + 4 * 5
print('Ответ:', result)

# Пример со скобками
result = 1 * (2 + 3) * 4 + 5
print('Ответ:', result)
```
Скриншот работы программы 2.

![Alt text](Term_2.png)

### Задание 03
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

print(my_favorite_movies[0:10])
print(my_favorite_movies[42:57])
print(my_favorite_movies[12:25])
print(my_favorite_movies[35:40])
```
Скриншот работы программы 3.

![Alt text](Term_3.png)

### Задание 04
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# моя семья (можно я не буду 9 человек расписывать)
my_family = ['Папа', 'Мама', 'Я']
my_family_height = [['Папа', 172], ['Мама', 169], ['Я', 179]]

print('Рост отца -', my_family_height[0][1], 'см')

family_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
print('Общий рост моей семьи -', family_height, 'см')
```
Скриншот работы программы 4.

![Alt text](Term_4.png)

### Задание 05
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Cписок животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Посадим медведя между львом и кенгуру
zoo.insert(1, 'bear')
print(zoo)

# Добавим птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)

# Уберём слона
zoo.remove('elephant')
print(zoo)

# Выведем на консоль в какой клетке сидит лев и жаворонок
print("Лев сидит в клетке №" + str(zoo.index('lion')+1))
print("Жаворонок сидит в клетке №" + str(zoo.index('lark')+1))
```
Скриншот работы программы 5.

![Alt text](Term_5.png)

### Задание 06
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Cписок песен группы Depeche Mode со временем звучания с точностью до долей минут
vsl = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
time_vsl = vsl[3][1] + vsl[5][1] + vsl[8][1]
print('Три песни звучат ' + str(round(time_vsl, 2)) + ' минут')

# Cловарь песен группы Depeche Mode
vsd = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
time_vsd = vsd['Sweetest Perfection'] + vsd['Policy of Truth'] + vsd['Blue Dress']
print('А другие три песни звучат ' + str(round(time_vsd, 2)) + ' минут')
```
Скриншот работы программы 6.

![Alt text](Term_6.png)

### Задание 07
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Зашифрованное сообщение
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

# Расшифрованное сообщение
w1 = secret_message[0][3]
w2 = secret_message[1][9:13]
w3 = secret_message[2][5:15:2]
w4 = secret_message[3][12:6:-1]
w5 = secret_message[4][20:15:-1]

print(w1, w2, w3, w4, w5)
```
Скриншот работы программы 7.

![Alt text](Term_7.png)

### Задание 08
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Садовые цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
# Луговые цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
# Множество цветов
garden_set = set(garden)
meadow_set = set(meadow)

# Все виды цветов
print(garden_set.union(meadow_set))

# Растут и там, и там
print(garden_set & meadow_set)

# Растут в саду, но не растут на лугу
print(garden_set - meadow_set)

# Растут на лугу, но не растут в саду
print(meadow_set - garden_set)
```
Скриншот работы программы 8.

![Alt text](Term_8.png)

### Задание 09
```python
# Словарь магазинов с распродажами
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Словарь цен на продукты
sweets = {
    'печенье':
    [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99}
    ],
    'конфеты':
    [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'пятерочка', 'price': 32.99}
    ],
    'карамель':
    [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'магнит', 'price': 41.99}
    ],
    'пирожное':
    [
        {'shop': 'магнит', 'price': 62.99},
        {'shop': 'пятерочка', 'price': 59.99}
    ]
}
print(sweets)
```
Скриншот работы программы 9.

![Alt text](Term_9.1.png)
![Alt text](Term_9.2.png)
![Alt text](Term_9.3.png)

### Задание 10
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Словарь кодов товаров
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Словарь списков количества товаров на складе.
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

sofas_quantity_1 = store[goods['Диван']][0]['quantity']
sofas_quantity_2 = store[goods['Диван']][1]['quantity']
sofas_quantity = sofas_quantity_1 + sofas_quantity_2
sofas_price_1 = store[goods['Диван']][0]['price']
sofas_price_2 = store[goods['Диван']][1]['price']
sofas_cost = (sofas_quantity_1 * sofas_price_1) + (sofas_quantity_2 * sofas_price_2)
print('Диван -', sofas_quantity, 'шт., стоимость', sofas_cost, 'руб.')

tables_quantity_1 = store[goods['Стол']][0]['quantity']
tables_quantity_2 = store[goods['Стол']][1]['quantity']
tables_quantity = tables_quantity_1 + tables_quantity_2
tables_price_1 = store[goods['Стол']][0]['price']
tables_price_2 = store[goods['Стол']][1]['price']
tables_cost = (tables_quantity_1 * tables_price_1) + (tables_quantity_2 * tables_price_2)
print('Стол -', tables_quantity, 'шт., стоимость', tables_cost, 'руб.')

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт., стоимость', lamps_cost, 'руб.')

chairs_quantity_1 = store[goods['Стул']][0]['quantity']
chairs_quantity_2 = store[goods['Стул']][1]['quantity']
chairs_quantity_3 = store[goods['Стул']][2]['quantity']
chairs_quantity = chairs_quantity_1 + chairs_quantity_2 + chairs_quantity_3
chairs_price_1 = store[goods['Стул']][0]['price']
chairs_price_2 = store[goods['Стул']][1]['price']
chairs_price_3 = store[goods['Стул']][2]['price']
chairs_cost = (chairs_quantity_1 * chairs_price_1) + (chairs_quantity_2 * chairs_price_2) + (chairs_quantity_3 * chairs_price_3)
print('Стул -', chairs_quantity, 'шт., стоимость', chairs_cost, 'руб.')
```
Скриншот работы программы 10.

![Alt text](Term_10.png)