# В этом задании требуется реализовать двоичное дерево поиска. Ваш класс BinarySearchTree должен поддерживать следующий интерфейс:
# 1. Инициализатор, который опционально может принимать значение, которое будет находиться в корне дерева.
# 2. append(value) добавляет в дерево новый элемент со значением value.
# 3. Класс должен поддерживать конструкцию value in tree, где value — число, а tree — экземпляр класса дерева.
# 4. Класс должен поддерживать механизм итерации. Итерирование соответствует обходу дерева в ширину.
# Примечания: В реализации обхода в ширину вам может пригодиться класс deque из модуля collections.

from collections import deque

class Node():
    def __init__(self, value):
        self.key = value
        self.lchild = None
        self.rchild = None

class BinarySearchTree():
    def __init__(self, value=None):
        if value is not None:
            self.__root = Node(value)
        else:
            self.__root = None
        # self._deque = deque([])

    def __iter__(self):
        print('iter')
        return self.__root

    def __next__(self):
        print('next')
        return self.__root.key

    def __get(self, value, curr):
        if curr:
            if curr.key == value:
                return curr
            elif curr.key > value:
                return self.__get(value, curr.lchild)
            else:
                return self.__get(value, curr.rchild)
        else:
            return None

    def __contains__(self, value):
        if self.__get(value, self._root) is None:
            return False
        else:
            return True

    def __str__(self):
        return f"{self.key}"

    def append(self, value):
        if self.__root is None:
            self.__root = Node(value)
        else:
            self.__append(value, self._root)

    def __append(self, value, curr):
        if curr.key > value:
            if curr.lchild is None:
                curr.lchild = Node(value)
            else:
                self.__append(value, curr.lchild)
        else:
            if curr.rchild is None:
                curr.rchild = Node(value)
            else:
                self.__append(value, curr.rchild)








if __name__ == '__main__':
    tree = BinarySearchTree()
    for v in [8, 3, 10, 1, 6, 4, 14, 13, 7]:
        tree.append(v)

    for v in [8, 12, 13]:
        print(v in tree)

    # print(*tree)

# # Результат работы
# # True
# # False
# # True
# # 8 3 10 1 6 14 4 7 13


# if __name__ == '__main__':
#     tree = BinarySearchTree()
#     for v in [5, 0, 6, 2, 1, 3]:
#         tree.append(v)

#     for v in [6, 12]:
#         print(v in tree)

#     print(*tree)

# # Результат работы
# # True
# # False
# # 5 0 6 2 1 3

