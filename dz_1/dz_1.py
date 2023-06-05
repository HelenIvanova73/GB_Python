# Задача 2: Найдите сумму цифр трехзначного числа.
n = int(input('Введите трехзначное число:'))
s = n // 100 + n // 10 % 10 + n % 10
print(f'Сумма цифр числа {n} равна {s}')

# Задача 2 c помощью строк
n = input('Введите трехзначное число:')
s = int(n[0]) + int(n[1]) + int(n[2])
print(f'Сумма цифр числа {n} равна {s}')

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в
# два раза больше журавликов, чем Петя и Сережа вместе?
s = int(input('Введите количество журавликов'))
print(f'Петя сделал {s // 4} журавликов, Катя - {s // 2}, Сережа - {s // 4}')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр
# равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
n = input('Введите номер вашего билета')
if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]):
    print('Cчастье есть, оно не может не есть!')
else:
    print('Повезет в другой раз..., maybe')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника)
m, n, k = int(input('m = ?')), int(input('n = ?')), int(input('k = ?'))
if (k % n == 0 or k % m == 0) and m * n >= k:
    print('yes')
else:
    print('no')