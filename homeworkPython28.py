weekly_schedule = {

    "Monday": ["Gym", "Work", "Read book"],

    "Tuesday": ["Meeting", "Work", "Study Python"],

    "Wednesday": ["Shopping", "Work", "Watch movie"],

    "Thursday": ["Work", "Call parents", "Play guitar"],

    "Friday": ["Work", "Dinner with friends"],

    "Saturday": ["Hiking", "Rest"],

    "Sunday": ["Family time", "Rest"]

}

iterator = iter(weekly_schedule)


while True:
    user_input = input("Нажмите 'Enter' для получения плана: ")
    if user_input in ["q", "quit", "cancel"]:
        print("Завершение программы")
        break

    try:
        day = next(iterator)

    except StopIteration:
        iterator = iter(weekly_schedule)
        day = next(iterator)

    print(f"{day}: {', '.join(weekly_schedule[day])}")

#-----------------------------------------------------------------------------------------------------------------------

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]


def all_products(*args):
    return (y.lower() for x in args for y in x)

for item in all_products(fruits, vegetables, dairy):
    print(item)

#-----------------------------------------------------------------------------------------------------------------------

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]


def combinations(cloth, color, size):
    import itertools

    result = (f"{c} - {col} - {s}" for c, col, s in itertools.product(cloth, color, size))
    return result

print(list(combinations(clothes, colors, sizes)))