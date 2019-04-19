# Напишите декоратор @counter, который позволял бы посчитать глубину рекурсии функции и количество рекурсивных вызовов функции.
# Декоратор должен создать два атрибута для функции:
# ncalls — число вызовов функции;
# rdepth — глубина рекурсии.
# Счётчики ncalls и rdepth должны обнуляться при каждом новом входе в рекурсию, см. примеры.

import time
import random
import functools


def counter(foo):
    if not  hasattr(counter, 'recurtion'):
        setattr(counter, 'recurtion', 0)
    if not  hasattr(foo, 'ncalls'):
        setattr(foo, 'ncalls', 0)
    if not  hasattr(foo, 'rdepth'):
        setattr(foo, 'rdepth', 0)
    @functools.wraps(foo)
    def wrapper(*arsg, **kwargs):
        if not counter.recurtion:
            setattr(wrapper, 'ncalls', 0)
            setattr(wrapper, 'rdepth', 0)
        wrapper.ncalls += 1
        counter.recurtion += 1
        result = foo(*arsg, **kwargs)
        wrapper.rdepth = max(counter.recurtion, wrapper.rdepth)
        counter.recurtion -= 1
        return result
    return wrapper

# @counter
# def func1():
#     return

# print(func1.__name__)

# if __name__ == "__main__":
#     func1()
#     print(func1.ncalls, func1.rdepth)

#     func1()
#     print(func1.ncalls, func1.rdepth)

# 1 1
# 1 1

# @counter
# def func2(n, steps):
#     if steps == 0:
#         return

#     func2(n + 1, steps - 1)
#     func2(n - 1, steps - 1)

# print(func2.__name__)

# if __name__ == "__main__":
#     func2(0, 5)
#     print(func2.ncalls, func2.rdepth)

#     func2(0, 3)
#     print(func2.ncalls, func2.rdepth)

# 63 6
# 15 4