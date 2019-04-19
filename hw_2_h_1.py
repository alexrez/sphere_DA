# В этом задании требуется реализовать двоичное дерево поиска. Ваш класс BinarySearchTree должен поддерживать следующий интерфейс:
# 1. Инициализатор, который опционально может принимать значение, которое будет находиться в корне дерева.
# 2. append(value) добавляет в дерево новый элемент со значением value.
# 3. Класс должен поддерживать конструкцию value in tree, где value — число, а tree — экземпляр класса дерева.
# 4. Класс должен поддерживать механизм итерации. Итерирование соответствует обходу дерева в ширину.
# Примечания: В реализации обхода в ширину вам может пригодиться класс deque из модуля collections.

from collections import deque


class BinarySearchTree():
    def __init__(self, value=None, left=None, right=None):
        self.key = value
        self.lchild = left
        self.rchild = right
        self.deq = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.deq is None:
            self.deq = deque([self])
        if self.key is None or not self.deq:
            self.deq = None
            raise StopIteration()
        node = self.deq.popleft()
        if node.lchild:
            self.deq.extend([node.lchild])
        if node.rchild:
            self.deq.extend([node.rchild])
        # print('kostil')
        return node

    def __contains__(self, value):
        if self.find(value, self) is None:
            return False
        else:
            return True

    def __str__(self):
        return str(self.key)

    def find(self, value, curr):
        if curr and curr.key is not None:
            if curr.key == value:
                return curr
            elif curr.key > value:
                return self.find(value, curr.lchild)
            else:
                return self.find(value, curr.rchild)
        else:
            return None


    def append(self, value, curr=None):
        if curr is None:
            curr = self
        if curr.key is None:
            curr.key = value
        else:
            if curr.key > value:
                if curr.lchild is None:
                    curr.lchild = BinarySearchTree(value)
                else:
                    self.append(value, curr.lchild)
            else:
                if curr.rchild is None:
                    curr.rchild = BinarySearchTree(value)
                else:
                    self.append(value, curr.rchild)



# if __name__ == '__main__':
#     tree = BinarySearchTree()
#     for v in [8, 3, 10, 1, 6, 4, 14, 13, 7]:
#         tree.append(v)

#     for v in [8, 12, 13]:
#         print(v in tree)

#     print(*tree)

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

# if __name__ == '__main__':
#     tree = BinarySearchTree()
#     for v in [8, 3, 10, 1, 6, 4, 14, 13, 7, 9]:
#         tree.append(v)

#     for v in [8, 0, 13]:
#         print(v in tree)

    # print(*tree)

# if __name__ == '__main__':
#     tree = BinarySearchTree()
#     for v in [5, 1, 7, 9, 11]:
#         tree.append(v)

#     # for v in [8, 0, 13]:
#     #     print(v in tree)

#     print(*tree)
#     print(*tree)

