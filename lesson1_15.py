cash = int(input("Введите значение выручки: "))
cost = int(input("Введите значение расходов: "))
if cash > cost:
    rent = (cash - cost) / cash
    print("Ваша фирма отработала с прибылью, рентабельность", rent)
    people = int(input("Введите количество сотрудников: "))
    print("Ваша выручка на одного сотрудника: ", (cash - cost) / people)
elif cash == cost:
    print("Вы отработали в '0'")
else:
    print("Ваша фирма работает в убыток")