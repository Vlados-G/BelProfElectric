# Task №2
# Вводим входных данных

n = int(input("Введите число n: "))
w = int(input("Введите число w: "))
d = int(input("Введите число d: "))
p = int(input("Введите число p: "))
s = 0
i = 1
# Посчитаем и сравним
for i in range(n):
    s += i * w
if(s == p):
    print(n)
else:
    print(abs((p - s))/d)
