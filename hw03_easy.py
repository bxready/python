__author__ = 'Алексей Коваленко'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    number = str(number).split('.')
    temp = (int(number[0] + number[1][0:ndigits]) + (1 if int(number[1][ndigits]) > 4 else 0)) / 10 ** ndigits
    return temp if int(temp) < temp else int(temp)


print('Задание 1')
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(0.6, 0))
print(my_round(399999.6, 0))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    digits = len(str(ticket_number)) // 2
    # сразу определимся, что про нечетность и четность номеров не сказано ничего,
    # поэтому поступаем как питон и будем принимать написанное явно
    # считаем суммы цифр с права и слева у любых чисел
    if sum(map(int, str(ticket_number)[0:digits])) == sum(map(int, str(ticket_number)[-digits:])):
        return True
    else:
        return False


print('\nЗадание 2')
print(lucky_ticket(123006))
print(lucky_ticket(123016))
print(lucky_ticket(12321))
print(lucky_ticket(123210))
print(lucky_ticket(436751))
print(lucky_ticket(436752))
