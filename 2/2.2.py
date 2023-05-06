# Выведите числа от 1 до 10 рекурсивно.
def numbers(n):
    if n == 0:
        return
    print(n)
    n -= 1
    numbers(n)


numbers(10)
