import math

#1
def my_sum():
    user_value = int(input("Введи число: "))
    result = 0
    if user_value < 1:
        print("Число должно быть больше 1")
    else:
        for i in range(user_value + 1):
            result += i
    print(result)
    return result


my_sum()

#3


def func():
    x = int(input("Введи число x: "))
    y = int(input("Введи число y: "))
    z = int(input("Введи число z: "))
    result = math.pow(((x ** 5 + 7)/abs(-6)*y), 1/3) / (7 - math.fmod(z, y))
    print(round(result, 3))
    return round(result, 3)

func()

#4
R1 = 1
R2 = 2

R_total = R1 + R2

rounded_R_total = round(R_total, 1)

print(rounded_R_total)

#5
def check(a, b, m, n):
    if a != 0:
        x = -b/a
        if m <= x <= n:
            return True
        else:
            return False
    elif a == 0 and b != 0:
        return False
    else:
        return True


#6
v = float(input("Введите скорость (в км/ч): "))
t = float(input("Введите время (в часах): "))

laps = t // (123 / v)

remaining_time = t % (123 / v)

distance = remaining_time * v

km = int(distance)

print(f"Спортсмен остановится на {km} километре.")

7

two_digit = int(input("Введите двузначное число: "))
three_digit = int(input("Введите трехзначное число: "))

digit_sum = two_digit // 10 + two_digit % 10
digit_product = (two_digit // 10) * (two_digit % 10)

print("Сумма:", digit_sum)
print("Произведение:", digit_product)

hundreds = three_digit // 100
tens = (three_digit // 10) % 10
ones = three_digit % 10
digit_sum = hundreds + tens + ones
digit_product = hundreds * tens * ones

#8

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

minimum = min(num1, num2, num3)
maximum = max(num1, num2, num3)
remaining = num1 + num2 + num3 - minimum - maximum

#9
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)

#10
team_name = input("Введите название футбольной команды: ")

print(team_name + " - чемпион!")

line = "-" * len(team_name)
print(line)

team_name_lower = team_name.lower()

print("Длина названия команды:", len(team_name))

has_p = "п" in team_name_lower
print("Наличие буквы 'п':", has_p)

count_a = team_name_lower.count("а")
print("Количество повторений буквы 'а':", count_a)

#11

state = str(input("государство"))
capital = str(input("столица"))

print(f"Государство - {state}, столица - {capital}")

#12
word = "объектно-ориентированный"

objekt = word[:6]
print("Слово 'объект':", objekt)

orientir = word[7:15]
print("Слово 'ориентир':", orientir)

tir = word[-3:]
print("Слово 'тир':", tir)

kot = word[10:13]
print("Слово 'кот':", kot)

renta = word[2:7]
print("Слово 'рента':", renta)