# task1
age = int(input("Введіть ваш вік: "))
if age < 18:
    print("Доступ заборонено!")
else:
    print("Доступ дозволено!")

# task2
stock = 20
quantity = int(input("Введіть кількість товару: "))
if quantity <= 0:
    print("Помилка: некоректна кількість!")
elif quantity > stock:
    print("На складі недостатньо товару!")
else:
    print("Ваше замовлення прийнято!")

# task3
password = input("Введіть пароль: ")
if len(password) < 8:
    print("Пароль надто короткий!")
elif password in ["password", "12345678"]:
    print("Пароль занадто простий!")
else:
    print("Вхід дозволено!")

# task4
temperature = float(input("Введіть температуру приміщення: "))
if temperature < 16:
    print("Температура занизька! Увімкніть обігрівач.")
elif temperature > 28:
    print("Температура зависока! Увімкніть кондиціонер.")
else:
    print("Температура комфортна.")

# task5
amount = float(input("Введіть суму поповнення: "))
if amount < 10:
    print("Мінімальна сума поповнення – 10 грн!")
elif amount > 3000:
    print("Сума поповнення занадто велика!")
else:
    print(f"Поповнення на суму {amount} грн виконано успішно!")
