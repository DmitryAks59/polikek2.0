# Классовая структура итогового проеткта 
(Подробнее об итоговом проекте в следующей работе)

В проекте 4 набора классов:
* characters - для работы с информацией о персонажах
* characters - для операций с инфорамацией о событиях произведения
* setting - класс для ведения каталога информации о сеттинге 

Прим: сеттинг - время, место и обстоятельства, в которых развиваются события произвдения. 
Сеттинг может быть определён каким-либо реальным историчским отрезком или местом, так и польностью выдуманнным. 

Пример использования в файле [prototype](/prototype.ipynb)

## Функция __str__ и __call__
```
character = Character()
name = 'Solomon Grundy'
role = 'main'
description = 'Man with short life'
character(name, role, description) #реализуется через def __call__(self)

print(character) #реализуется через def __str__(self)
```

Вывод

Имя: Solomon Grundy

Роль: main

Описание: Man with short life



## Функция __repr__
```
week = Timeline('Life of Solomon Grundy', '2022-10-31', '2022-11-06')
print(week)
print(week.__repr__())
```

Life of Solomon Grundy started at 2022-10-31 00:00:00 and ended at 2022-10-31 00:00:00

{'name': 'Life of Solomon Grundy', 'start_date': Timestamp('2022-10-31 00:00:00'), 'end_date': Timestamp('2022-10-31 00:00:00')}
