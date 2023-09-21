import math


def find_lcm(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm


def find_gcd(numbers):
    gcd = numbers[0]
    for num in numbers[1:]:
        gcd = math.gcd(gcd, num)
    return gcd


numbers_list = [6, 8, 12, 24]
given_list = [33, 56, 78, 3, 7, 11, 77]
lcm = find_lcm(given_list)
gcd = find_gcd(given_list)
print(lcm, gcd)

 #2
def count_sentences_with_digits(sentences):
    count = 0
    for sentence in sentences:
        for char in sentence:
            if char.isdigit():
                count += 1
                break
    return count


sentences = [
    "Нет цифр",
    "2 цифры: 1 и 2",
    "Цифр много не бывает:1,2,3,4,55"
]

count = count_sentences_with_digits(sentences)
print(f"Количество предложений с цифрами: {count}")

# #3
def draw_frame(s, k):
    frame_width = len(s) + 4
    frame_top = k * frame_width
    frame_middle = f"{k} {s} {k}"
    frame_bottom = k * frame_width

    print(frame_top)
    print(frame_middle)
    print(frame_bottom)


s = "Текст в рамке"
k = "*"
draw_frame(s, k)

# #4
def char_stats(sentence):
    sentence = sentence.lower()
    stats = {}

    for char in sentence:
        if char in stats:
            stats[char] += 1
        else:
            stats[char] = 1

    return stats


frase = "Для введенного предложения выведите статистику символ=количество"
stats = char_stats(frase)
for char, count in stats.items():
    print(f"{char} = {count}")

#5
def encrypt_caesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('а') if char.islower() else ord('А')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 32 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('а') if char.islower() else ord('А')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 32 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

original_text = input("Введите строку: ")

shift = int(input("Введите сдвиг: "))

encrypted_text = encrypt_caesar(original_text, shift)
print("Зашифрованная строка:", encrypted_text)

decrypted_text = decrypt_caesar(encrypted_text, shift)
print("Расшифрованная строка:", decrypted_text)

#6

def return_tuple(*args):
    negatives = sorted([x for x in args if x < 0], reverse=True)
    positives = sorted([x for x in args if x >= 0])
    return (negatives, positives)


result = return_tuple(1, 2, 5, -4, 12, 6, 222, -76)
print(result)

#7
def is_palindrome(string):
    string = string.lower()
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True

user_input = input("Введите строку: ")

if is_palindrome(user_input):
    print("Введенная строка является палиндромом.")
else:
    print("Введенная строка не является палиндромом.")

#8


def guess_number():
    lower_bound = 1
    upper_bound = 100
    tries = 0

    while True:
        guess = (lower_bound + upper_bound) // 2
        tries += 1

        answer = int(input(f"Твое число равно, меньше или больше, чем число {guess}? (1-равно, 2-больше, 3-меньше): "))

        if answer == 1:
            print("Число угадано!")
            break
        elif answer == 2:
            lower_bound = guess + 1
        elif answer == 3:
            upper_bound = guess - 1

        if tries >= 7:
            print("Я использовал все попытки")
            break

print("Загадай число: ")
guess_number()


#10
def is_magic_date(day, month, year):
    if day * month == year % 100:
        return True
    else:
        return False


def check():
    century = int(input("Введите год XX века: "))

    for year in range(century * 100, (century + 1) * 100):
        for month in range(1, 13):
            for day in range(1, 32):
                if day <= 31 and month <= 12:
                    if is_magic_date(day, month, year):
                        print(f"{day:02d}.{month:02d}.{year}")
check()
