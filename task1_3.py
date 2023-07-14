"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

while True:
    num = int(input('Введите положительное число до 100000: '))
    if num < 1 or num > 100000:
        print('Число не входит в заданный диапазон')
        continue
    else:
        count = 0
        for i in range(2, num // 2 + 1):
            if (num % i == 0):
                count += 1
        if (count == 0):
            print("Число простое")
            break
        else:
            print("Число составное")
            break
