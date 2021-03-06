# За линией фронта
# Роберт успешно справился с вылазкой в тыл врага и раздобыл одну полоску из тетради в клетку длиной N клеток.
# Кроме того в руки Роберта попал лист изменений этой полоски. Враг выбирал две позиции i и j и записывал между ними новое сообщение
# (оба конца/позиции включены). При этом, если новое сообщение накладывалось на старое, то старое становилось навсегда утерянным.
# Напишите программу, которая определит, сколько на полоске осталось не утерянных сообщений.

# Формат входных данных: Первая строка содержит число N (1 ≤ N ≤ 10000) — длину клечатой полоски. Вторая строка содержит число K (1 ≤ K ≤ 1000) — 
# число сообщений. Следующие K строк содержат пары чисел i и j (1 ≤ i ≤ j ≤ N), задающих начало и конец сообщений.

# Формат результата: Выведите единственное число — количество не утерянных сообщений.

n = int(input())
strip = [0]*(n+1)

k = int(input())
# for it in range(1, k+1):
# 	i, j = input().split(' ')
# 	strip[int(i)-1] = strip[int(j)-1] = it

# count = 0
# tmp = 0
# for unit in strip:
# 	if tmp < unit:
# 		tmp = unit
# 	elif tmp == unit and unit != 0:
# 		count+=1
# 		tmp = 0

messages = [-1]*(k+1)
for it in range(1, k+1):
	i, j = input().split(' ')
	messages[it] = int(j) - int(i) + 1
	for step in range(int(i)-1, int(j)):
		strip[step] = it
print(messages)

count = 0
tmp = 0
mes_len = 0
for unit in strip:
	if tmp != unit:
		if mes_len == messages[tmp]:
			count+=1
		tmp = unit
		mes_len = 0
	mes_len+=1

print(*strip)
print(count)