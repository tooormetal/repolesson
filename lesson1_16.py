a = int(input("Введите стартовое количество км: "))
b = int(input("Введите финальное количество км: "))
i = 1
while a < b:
    a *= 1.1
    i += 1
print("Спортсмен добьется цели на %d день" % i)
