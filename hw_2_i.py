# Класс FragileDict должен реализовывать следующий интерфейс:
# 1. Инициализатор опционально может принимать на вход словарь, содержимое которого будет храниться в «хрупком словаре».
# В конструкторе заполняются два атрибута: _data — хранилище с данными, _lock — булев флаг, показывающий разрешено ли редактировать хранилище.
# Других полей быть НЕ должно.
# 2. Из любого экземпляра класса FragileDict можно читать данные аналогично тому, как это делается для словарей, например, d['key'].
# Если ключ (key) отсутствует, то бросается исключение KeyError(key), как если бы это был просто словарь.
# 3. Класс FragileDict должен поддерживать механизм менеджера контекста.
# 4. В экземпляры класса можно записывать данные аналогично тому, как это делается для словарей, например, d['key'] = value.
# Однако разрешается это делать только внутри контекста. Если этот контракт нарушается, то бросается исключение RuntimeError("Protected state").
# При входе в контекст разрешается создавать любые атрибуты класса, но на выходе из контекста никаких сторонних атрибутов быть не должно.
# 5. Если внутри контекста возникло исключение, то данные не записываются. На выходе из контекста «словарь» должен иметь точно такое же состояние, 
# как и на входе. Само исключение подавляется, и пишется сообщение об ошибке "Exception has been suppressed.".
# 6. Класс должен поддерживать проверку наличия ключа в формате key in d, где key — некоторый ключ, а d — экземпляр класса «хрупкого словаря».
# Примечания: Как вы вероятно помните, в Python все объекты передаются по ссылке. Для обеспечения большей безопасности вашего хранилища
# вам должен пригодиться модуль copy. Вспомните про разницу между поверхностными копированием (shallow copy) и глубоким копированием (deep copy).

import copy


class FragileDict():
    def __init__(self, d=None):
        if d is None:
            self._data = dict()
        else:
            self._data = copy.deepcopy(d)
        self._lock = True # заблокировано

    def __getitem__(self, key):
        if not self._lock:
            if key in self.__new_data:
                return self.__new_data[key]
            else:
                raise KeyError(key)
        else:
            if key in self._data:
                return copy.deepcopy(self._data[key])
            else:
                raise KeyError(key)

    def __setitem__(self, key, value):
        if not self._lock:
            self.__new_data.update({key: value})
        else:
            raise RuntimeError("Protected state")

    def __enter__(self):
        self._lock = False
        self.__new_data = copy.deepcopy(self._data)
        return self

    def __exit__(self, exp_type, exp_value, exp_tr):
        copied_data = copy.deepcopy(self.__new_data)
        del self.__new_data
        self._lock = True
        if exp_type is not None:
            print("Exception has been suppressed.")
            return True
        else:
            self._data.update(copied_data)

    def __contains__(self, key):
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False



# # Входные данные
# d = FragileDict()
# d = FragileDict({'key': 5})

# with d:
#     d['key'] = 6
#     d['ord'] = 7

# print(d['key'])
# print(d['ord'])


# # Результат работы
# # 6
# # 7

# # Входные данные
# d = FragileDict({'key': 5})

# try:
#     d['key'] = 6
# except RuntimeError as e:
#     print(e)

# try:
#     d['ord'] = 7
# except RuntimeError as e:
#     print(e)

# print(d['key'] == 5)
# print('ord' not in d)

# # Результат работы
# # Protected state
# # Protected state
# # True
# # True

# # Входные данные
# d = FragileDict({'key': 5})

# with d:
#     d['key'] = 6
#     print(d['key'])
#     d['ord'] = 7
#     print('ord' in d and d['ord'] == 7)
#     raise Exception()

# print(d['key'])
# print('ord' not in d)

# # Результат работы
# # 6
# # True
# # Exception has been suppressed.
# # 5
# # True

# # Входные данные
# d = FragileDict({'key': []})

# with d:
#     a = d['key']
#     d['key'].append(10)
#     a.append(10)


# a.append(10)
# print(a == [10, 10, 10] and d['key'] == [10, 10])

# # Результат работы
# # True

# with FragileDict() as d:
#     d['key'] = 6
#     print(d['key'])
#     d['ord'] = 7
#     print('ord' in d and d['ord'] == 7)




# a = {}
# d = FragileDict(a)
# a.update({'q': 3})

# print(a)
# print(d.__dict__)




