# можно вычислить факториал n (произведение
# всех положительных целых чисел меньше или равных n), используя алгоритм
# с постоянной пространственной сложностью О(1):
x = 1
n = 5
for i in range(1, n + 1):
    x = x * i
    print(x)

x = 1
n = 5
a_list = []
for i in range(1, n + 1):
    a_list.append(x)
x = x * i
print(a_list)
