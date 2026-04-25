import itertools

weekly_schedule = {

    "Monday": ["Gym", "Work", "Read book"],

    "Tuesday": ["Meeting", "Work", "Study Python"],

    "Wednesday": ["Shopping", "Work", "Watch movie"],

    "Thursday": ["Work", "Call parents", "Play guitar"],

    "Friday": ["Work", "Dinner with friends"],

    "Saturday": ["Hiking", "Day off"],

    "Sunday": ["Family time", "Day off"]

}

iterators = itertools.cycle(weekly_schedule)

while True:
    user_input = input("Нажмите 'Enter' для получения плана: ")
    if user_input in ["q", "quit", "cancel"]:
        print("Завершение программы")
        break

    day = next(iterators)
    print(f"{day}: {', '.join(weekly_schedule[day])}")

#-----------------------------------------------------------------------------------------------------------------------

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]


def all_products(*args):
    merged = itertools.chain(*args)
    return (x.lower() for x in merged)

for item in all_products(fruits, vegetables, dairy):
    print(item)

#-----------------------------------------------------------------------------------------------------------------------

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]


def combinations(cloth, color, size):


    result = (f"{c} - {col} - {s}" for c, col, s in itertools.product(cloth, color, size))
    return result

print(list(combinations(clothes, colors, sizes)))