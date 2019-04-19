# 'python' -> ['pppp', 'yyyy', 'tttt', 'hhhh', 'oooo', 'nnnn']
def solution1(word):
    return [letter * 4 for letter in word]

# 'python' -> ['p', 'yy', 'ttt', 'hhhh', 'ooooo', 'nnnnnn']
def solution2(word):
    return [letter * (i+1) for i, letter in enumerate(word)]

# range(16) -> [0, 3, 5, 6, 9, 10, 12, 15]
def solution3(arg):
    return [numb for numb in arg if (numb % 3 == 0 or numb % 5 == 0)]

# [[1, 2, 3], [4, 5, 6, 7], [8, 9], [0]] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def solution4(args):
    return [a for arg in args for a in arg]

# 15 -> [(3, 4, 5), (5, 12, 13), (6, 8, 10), (9, 12, 15)]
def solution5(n):
    return [(a, b, c) for a in range(1, n) for b in range(a, n) for c in range(b, n+1) if c**2 == a**2 + b**2]

# ([0, 1, 2], [0, 1, 2, 3, 4]) -> [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
def solution6(args):
    return [[num + i for num in args[1]] for i in args[0]]

# [[1, 2], [3, 4], [5, 6]] -> [[1, 3, 5], [2, 4, 6]]
# [[1, 3, 5], [2, 4, 6]] -> [[1, 2], [3, 4], [5, 6]]
def solution7(args):
    # return [[arg[i] for arg in args] for i in range(len(args[0]))]
    return [[*i] for i in zip(*args)]

# ["0", "1 2 3", "4 5 6 7", "8 9"] -> [[0], [1, 2, 3], [4, 5, 6, 7], [8, 9]]
def solution8(args):
    return [list(map(int, stri.split(' '))) for stri in args]

# range(0, 7) -> {'a': 0, 'b': 1, 'c': 4, 'd': 9, 'e': 16, 'f': 25, 'g': 36}
def solution9(arg):
    return {chr(ord('a') + i): i**2 for i in arg}

# ['Alice', 'vova', 'ANTON', 'Bob', 'kAMILA', 'CJ', 'ALICE', 'Nastya'] -> {'Alice', 'Anton', 'Kamila', 'Nastya', 'Vova'}
def solution10(args):
    return set(sorted(s.capitalize() for s in args if len(s) > 3))
    # return set(sorted(set(s.capitalize() for s in args if len(s) > 3)))


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

# print(solutions['solution10'](['Alice', 'vova', 'ANTON', 'Bob', 'kAMILA', 'CJ', 'ALICE', 'Nastya']))

# solutions = {
#     'solution1': lambda word: [letter*4 for letter in word],
#     'solution2': lambda word: [letter*(i+1) for i, letter in enumerate(word)],
#     'solution3': lambda arg: [numb for numb in arg if (numb % 3 == 0 or numb % 5 == 0)],
#     'solution4': lambda args: [a for arg in args for a in arg],
#     'solution5': lambda n: [(a, b, c) for a in range(1, n) for b in range(a, n) for c in range(b, n+1) if c**2 == a**2 + b**2],
#     'solution6': lambda args: [[num+i for num in args[1]] for i in args[0]],
#     'solution7': lambda args: [[*i] for i in zip(*args)],
#     'solution8': lambda args: [list(map(int, stri.split(' '))) for stri in args],
#     'solution9': lambda arg: {chr(ord('a') + i): i**2 for i in arg},
#     'solution10': lambda args: set(sorted(s.capitalize() for s in args if len(s) > 3)),
# }

# print(solutions['solution1']('python'))