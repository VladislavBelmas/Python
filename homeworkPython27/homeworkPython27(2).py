import os

drive = input("Введите название вашего диска (C, D, E и тд): ").strip().upper()
file_name = input("Введите имя файла для поиска: ").strip()
found = False


for root, _, files in os.walk(f"{drive}:\\"):
    if found:
        break

    for file in files:
        if file == file_name:
            print(f'Файл {file} был найден')
            found = True
            os.chdir(root)
            break


if not found:
    raise FileNotFoundError("Файл не найден")


with open(file_name) as file:
    open(f'unique_{file_name}', 'w')
    for line in file:
        if line not in open(f'unique_{file_name}').read():
            open(f'unique_{file_name}', "a").write(line)


open(f'unique_{file_name}').close()
print(f"Уникальные строки сохранены в unique_{file_name}.")





