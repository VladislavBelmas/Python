text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

for i, text in enumerate(text_list):
    if " " in text.strip():
        text_list.remove(text)
    text_list[i] = text_list[i].lower()

print(text_list)

#-----------------------------------------------------------------------------------------------------------------------

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
discount = 0.17#int(input("Enter the discount %: ")) / 100
result = [f'{"Товар":<14} {"Старая цена":>10} {"Новая цена":>15}']

for item in products:
    product, price = item
    new_price = price - price * discount
    item.append(new_price)
    result.append(f"{product:<14} {price:>10.2f}$ {new_price:>14.2f}$")

print("\n".join(result))

#-----------------------------------------------------------------------------------------------------------------------
#Изначальный вариант решения

for product in products:
    product.append(product[1] - product[1] * discount)
    result.append(f"{product[0]:<14} {product[1]:>10.2f}$ {product[2]:>14.2f}$")

print("\n".join(result))