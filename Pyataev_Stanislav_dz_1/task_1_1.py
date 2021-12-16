# Вывод информации о промежутке времени в зависимости от его продолжительности в секундах

duration = int(input("Введите количество секунд, которое необходимо перевести: "))

answ = []            # пустой список с ответом

d_s = 60 * 60 * 24   # количество секунд в дне
h_s = 60 * 60        # количество секунд в часе
m_s = 60             # количество секунд в минуте

while duration != 0:
    if duration // d_s > 0:       # расчет количества дней
        d = duration // d_s
        duration -= d * d_s
        answ.append(f"{d} дн.")
    elif duration // h_s > 0:     # расчет количества часов
        h = duration // h_s
        duration -= h * h_s
        answ.append(f"{h} час.")
    elif duration // m_s > 0:     # расчет количества минут
        m = duration // m_s
        duration -= m * m_s
        answ.append(f"{m} мин.")
    else:                         # расчет количества секунд
        s = duration
        answ.append(f"{s} сек.")
        break

print("Заданное Вами количество секунд равно: ")

for i in answ:
    print(i, end=" ")
