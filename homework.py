# 2.3 Цикл for
# Задача 2.3.3
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(end='\t')
for j in range(c, d+1):
    print(j, end='\t')
print()

for i in range(a, b+1):
    print(i, end='\t')
    for j in range(c, d+1):
        print(i*j, end='\t')
    print()

# Вывести сумму всех нечетных чисел от a до b (включая обе границы)
# Решение 1
a, b = input().split()
a = int(a)
b = int(b)
s = 0
for i in range(a, b+1):
    if i % 2 == 1:
        s += i
print(s)

# Решение 2
a, b = input().split()
a = int(a)
b = int(b)
s = 0
if a % 2 == 0: # проверка числа на четность
    a += 1
for i in range(a, b+1, 2):
    s += i
print(s)

# Решение 3
a, b = (int(i) for i in input().split()) # применяем int для каждого i из последовательности
s = 0
if a % 2 == 0: # проверка числа на четность
    a += 1
for i in range(a, b+1, 2):
    s += i
print(s)

# Задача 2.3.7
a = int(input())
b = int(input())
s = 0
i = 0

for j in range(a, b+1):
    if j % 3 == 0:
        s += j
        i += 1
print(s/i)

# 2.4 Строки и символы
genome = input()
print(genome.count('C')) # Выводит количество вхождений в подстроку

# Задача 2.4.3
genome = input()
l = len(genome)
x = genome.upper().count('G'.upper())
y = genome.upper().count('C'.upper())
print(((x+y)/l)*100)

# Дана геномная последовательность. Проверить, является ли она палиндромом

# Задача 2.4.7
s = input()
i = 0
j = 0

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        i += 1
        j += 1
    elif s[i] != s[i+1]:
        i += 1
        j += 1
        print(s[i-1] + str(j), end='')
        j = 0
print(s[i] + str(j+1), end='')
