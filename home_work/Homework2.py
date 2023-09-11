#1
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
print(a.count(5))

new_list = [i for i in a if i != 5]
new_list.extend(c)
print(new_list.count(3))
print(new_list)



#2
class_a = list(range(160, 177, 2))

class_b = list(range(162, 181, 3))

both = class_a + class_b

both.sort()

print(both)



#3
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

inventory = {}
for item in shop:
    name, price = item
    if name in inventory:
        inventory[name]['count'] += 1
        inventory[name]['total_price'] += price
    else:
        inventory[name] = {'count': 1, 'total_price': price}

requested_item = input("Введите название детали: ")
requested_item_lower = requested_item.lower()

if requested_item_lower in inventory:
    count = inventory[requested_item_lower]['count']
    total_price = inventory[requested_item_lower]['total_price']
    print(f"Количество: {count}")
    print(f"Общая стоимость: {total_price}")
else:
    print("Не найдено.")


#4

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

name = input("Ваше имя: ")
action = input("Действие: ")

def switch(action):
    if action == "Пришел":
        if len(guests) < 6:
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет")
    elif action == "Ушел":
        print(f"Пока, {name}!")
        guests.remove(name)
    else:
        print("Пора спать")

switch(action)



#5

violator_songs = [
    ['World in My Eyes', 4,86],
    ['Sweetest Perfection', 4,43],
    ['Personal Jesus', 4,56],
    ['Halo', 4,9],
    ['Waiting for the Night', 6,7],
    ['Enjoy the Silence', 4,20],
    ['Policy of Truth', 4,76],
    ['Blue Dress', 4,29],
    ['Clean', 5,83]
]

list_song = []
summ = 0
number_of_songs = int(input('Сколько песен выбрать? '))
for i in range(number_of_songs):
    song = input(f'Название {i + 1}-й песни: ')
    list_song.append(song)
for j in violator_songs:
    if j[0] in list_song:
        summ += j[1]
print(f'\nОбщее время звучания песен {summ} минуты')

#6
first_list = []
second_list = []

first_list_counter = 1
second_list_counter = 1
while first_list_counter <= 3:
    given_number = int(input(f"Введите {first_list_counter}-е число для первого списка: "))
    first_list.append(given_number)
    first_list_counter += 1

while second_list_counter <= 7:
    given_number_2 = int(input(f"Введите {second_list_counter}-е число для второго списка: "))
    second_list.append(given_number_2)
    second_list_counter += 1

print(first_list)
print(second_list)

first_list.extend(second_list)

print(set(first_list))

8
def last_person_standing(N, K):

    circle = list(range(1, N + 1))
    current_index = 0

    while len(circle) > 1:
        current_index = (current_index + K - 1) % len(circle)
        removed_person = circle.pop(current_index)

    return circle[0]


N = int(input("Кол-во человек: "))
K = int(input("Какое число в считалке? "))

result = last_person_standing(N, K)
print(f"Остался человек под номером {result}")

#9
N = int(input("Кол-во друзей: "))
K = int(input("Долговых расписок: "))

balances = {}

for i in range(K):
    print(f"{i + 1}-я расписка")
    debitor = int(input("Кому: "))
    creditor = int(input("От кого: "))
    amount = int(input("Сколько: "))


    balances[debitor] = balances.get(debitor, 0) - amount
    balances[creditor] = balances.get(creditor, 0) + amount

print("Баланс друзей:")
for friend in range(1, N + 1):
    print(f"{friend}: {balances.get(friend, 0)}")


#10
N = int(input("Кол-во чисел: "))

sequence = []

for i in range(N):
    num = int(input("Число: "))
    sequence.append(num)

def is_symmetric(seq):
    return seq == seq[::-1]

min_count = 0
while not is_symmetric(sequence):
    min_count += 1
    sequence.insert(len(sequence) - min_count, sequence[min_count - 1])

added_numbers = sequence[-min_count:]

print("Последовательность:", sequence)
print("Нужно приписать чисел:", min_count)
print("Сами числа:", added_numbers)
