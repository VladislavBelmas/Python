numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
summary = 0
for number in numbers:
    if number > 0:
        summary += number

print(f"Сумма положительных чисел: ${summary:,.2f}")

data_list = [
 "John 23 12345.678",
 "Alice 30 200.50",
 "Bob 35 15000.3",
 "Charlie 40 500.75"
]
for string in data_list:
    item = string.split()
    print("Имя: {0:10} | Возраст: {1:3} | Баланс: {2:10.2f}".format(item[0], item[1], float(item[2])))