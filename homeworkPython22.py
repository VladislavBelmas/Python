#1
orders = [

    {"product": "Laptop", "price": 1200},

    {"product": "Mouse", "price": 50},

    {"product": "Keyboard", "price": 100},

    {"product": "Monitor", "price": 300},

    {"product": "Chair", "price": 800},

    {"product": "Desk", "price": 400}

]


print(sorted(list(map((lambda n: n['product']), filter(lambda d: d["price"] > 500, orders)))))

#-----------------------------------------------------------------------------------------------------------------------
#2
sales = [

    ("Laptop", 5, 1200),

    ("Mouse", 50, 20),

    ("Keyboard", 30, 50),

    ("Monitor", 10, 300),

    ("Chair", 20, 800)

]


print(dict(sorted(((x[0], x[1] * x[2]) for x in sales), key=lambda x: x[1], reverse=True)))


