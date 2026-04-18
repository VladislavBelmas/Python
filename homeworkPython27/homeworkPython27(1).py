import os

search_file = input("Введите имя файла для поиска: ").strip()
search_word = input("Введите ключевое слово: ").strip()
add_lines = []
found = False

for root, _, files in os.walk("C:\\"):
    if found:
        break

    for file in files:
        if file == search_file:
            print(f'Файл {file} был найден')
            os.chdir(root)
            found = True
            break

if not found:
    raise FileNotFoundError("Файл не найден")


with open(search_file) as file:
    for line in file:
        if search_word in line.split():
            add_lines += [line]

if not add_lines:
    raise Exception("Совпадений по слову не найдено")

with open(f'{search_word}_{search_file}', "w") as file:
    file.write(''.join(add_lines))

print(f"Строки, содержащие '{search_word}', сохранены в {search_word}_{search_file} в той же директории.")