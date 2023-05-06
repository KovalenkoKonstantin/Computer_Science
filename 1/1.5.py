# Ниже приведен пример угадывания пароля со сложностью О(10**n):
pin = 931
n = len(str(pin))
# n = 3
for i in range(10 ** n):
    if i == pin:
        print(i)
