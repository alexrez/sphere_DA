import re
import operator
from functools import reduce

# ['12', '25.6', '84,02', '  69-91'] -> [21, 652, 2048, 1996]
def solution1(args):
    return list(map(lambda x: int(re.sub(r'\D', '', x[::-1])), args))

# zip(range(2, 5), range(3, 9, 2)) -> [6, 15, 28]
def solution2(arg):
    return list(map(lambda t: t[0]*t[1], arg))

# range(20) -> [0, 2, 5, 6, 8, 11, 12, 14, 17, 18]
def solution3(arg):
    return list(filter(lambda x: x%6 in [0, 2, 5], arg))

# ['', 25, None, 'python', 0.0, [], ('msu', '1755-01-25')] -> [25, 'python', ('msu', '1755-01-25')]
def solution4(args):
    return list(filter(lambda x: x, args))

# Добавьте к каждому элементу списка rooms поле square, показывающее площадь комнаты. Элементы списка rooms ДОЛЖНЫ обновиться!
rooms = [
    {"name": "комната1", "width": 2, "length": 4},
    {"name": "комната2", "width": 2.5, "length": 5.6},
    {"name": "кухня", "width": 3.5, "length": 4},
    {"name": "туалет", "width": 1.5, "length": 1.5},
]
def solution5(rooms):
    return list(map(lambda room: room.update({"square": room["width"] * room["length"]}) or room, rooms))

# Добавьте к каждому элементу списка rooms поле square, показывающее площадь комнаты. 
# Элементы исходного списка rooms НЕ ДОЛЖНЫ обновиться! Порядок элементов в результирующем списке должен совпадать с порядком в исходном списке.
def solution6(rooms):
    return list(map(lambda room: room.update({"square": room["width"] * room["length"]}) or room, (map(lambda r: dict(r), rooms))))

# Найдите пересечение всех множеств. Используйте функцию reduce.
# [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}, {3, 4, 5, 6, 7}] -> {3, 4, 5}
def solution7(args):
    return reduce(lambda x, y: x & y, args)

# [1, 2, 1, 1, 3, 2, 3, 2, 4, 2, 4] -> {1: 3, 2: 4, 3: 2, 4: 2}
def solution8(args):
    return reduce(lambda d, key: operator.setitem(d, key, d.get(key)+1) or d, args, dict.fromkeys(args, 0))

# Выведите имена студентов, чей GPA > 4.5.
students = [
    {'name': 'Alina', 'gpa': 4.57},
    {'name': 'Sergey', 'gpa': 5.0},
    {'name': 'Nastya', 'gpa': 4.21},
    {'name': 'Valya', 'gpa': 4.72},
    {'name': 'Anton', 'gpa': 4.32},
]
# students -> ['Alina', 'Sergey', 'Valya']
def solution9(students):
    return list(map(lambda s: s['name'], filter(lambda stud: stud['gpa'] > 4.5, students)))

# Счастливые билетики по-питерски.
# Билетик называется счастливым, если сумма цифр на четных местах равна сумме цифр на нечетных. Из исходного списка выведите только счастливые билетики.
# Пример: ['165033', '477329', '631811', '478117', '475145', '238018', '917764', '394286'] -> ['165033', '475145', '238018']
def solution10(tickets):
    return list(filter(lambda ticket: sum(list(map(int, list(ticket[::2])))) == sum(list(map(int, list(ticket[1::2])))), tickets))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}

# print(solutions['solution8']([1, 2, 1, 1, 3, 2, 3, 2, 4, 2, 4]))
