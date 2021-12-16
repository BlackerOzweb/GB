# Создать список, состоящий из кубов нечетных чисел от 1 до 1000
my_list = []
for i in range(1, 1001):
    if i % 2 == 1:
        numb = i ** 3
        my_list.append(numb)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
sum_all = 0
for num in my_list:
    list_numb = [int(a) for a in str(num)] # создаем список цифр числа
    sum_numer = 0
    for numer in list_numb:
        sum_numer += numer
    if sum_numer % 7 == 0:
        sum_all += num
print(f"Сумма чисел, сумма цифр которых делится нацело на 7, равна {sum_all}.")

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7, не создовая список
sum_all = 0
for num in my_list:
    num += 17                   # прибавляем заданное число
    sum_numer = 0
    for numer in str(num):
        sum_numer += int(numer)
    if sum_numer % 7 == 0:
        sum_all += num
print(f"Сумма чисел плюс 17, сумма цифр которых делится нацело на 7, равна {sum_all}.")