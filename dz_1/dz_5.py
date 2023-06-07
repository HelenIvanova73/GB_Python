'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.'''

print('Task 26')
def exponentator(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / (a * exponentator(a, -b - 1))
    else:
        return a * exponentator(a, b - 1)
 
a = int(input('Введите основание степени, а: '))
b = int(input('Введите показатель степени, b: '))
print( f'{a} ^ {b} = {exponentator(a, b)}')




'''Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций
допускаются только +1 и -1. Также нельзя использовать циклы.'''

print('Task 28')
def summator(a, b):
    if a == 0:
        return b
    else:
        return summator(a - 1, b + 1)
        
a = int(input('Введите а: '))
b = int(input('Введите b: '))
print( f'{a} + {b} = {summator(a, b)}')  