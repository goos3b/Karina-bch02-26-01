import math

print("Расчёт скорости резания")

mode = int(input("Режим (1 — черновая, 2 — получистовая, 3 — чистовая): "))

if mode == 1:
    k = 1.0
    mode_name = "черновая обработка"
elif mode == 2:
    k = 0.85
    mode_name = "получистовая обработка"
else:
    k = 0.7
    mode_name = "чистовая обработка"

# Ввожу диаметры с проверкой
f = False
while not f:
    D = float(input("Диаметр заготовки D, мм (1–500): "))
    if 1 <= D <= 500:
        f = True
    else:
        print("Ошибка: диаметр должен быть от 1 до 500 мм")
f = False
while not f:
    n = float(input("Частота вращения n, об/мин (50–3000): "))
    if 50 <= n <= 3000:
        f = True
    else:
        print("Ошибка: частота должна быть от 50 до 3000 об/мин")

V = math.pi * D * n / 1000
V_adj = V * k

if D < 10:
    d_class = "малый диаметр"
elif D <= 100:
    d_class = "нормальный диаметр"
else:
    d_class = "крупный диаметр"
print("\nРезультаты:")
print(f"Режим: {mode_name}")
print(f"Скорость резания V = {round(V, 2)} м/мин")
print(f"Скорректированная скорость V_adj = {round(V_adj, 2)} м/мин")
print(f"Класс диаметра: {d_class}")