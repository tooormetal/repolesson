number = int(input("Введите число: "))
num = 0
while (number // 10) > 1:
    i = number % 10
    if num < i:
        num = i
    number = number // 10
print (num)



