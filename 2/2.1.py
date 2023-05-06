# Ниже представлен итеративный алгоритм, который вычисляет факториал
# числа n:
def factorial(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n = n - 1
    return the_product


# А вот как написать этот же алгоритм рекурсивно:
def factorial_alt(n):
    if n == 0:
        return 1
    return n * factorial_alt(n - 1)


print(factorial(5))
print(factorial_alt(5))
