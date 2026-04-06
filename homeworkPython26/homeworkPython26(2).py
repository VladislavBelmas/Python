import os
import sys

if len(sys.argv) != 3:
    print('Usage: script.py <path> <extension>')
    sys.exit(1)


path = sys.argv[1]
file_type = sys.argv[2]
result = []


if not os.path.exists(path):
    print('Enter correct path')
    sys.exit(1)



for root, _, files in os.walk(path):
    for file in files:
        if file.endswith(file_type):
            result.append(os.path.join(root,file))


print(f'Files with type "{file_type}":')


if not result:
    print("Not found")
    sys.exit(1)


for file in result:
    print(f'- {file}')


action = input("Wanna delete? (y/n): ").strip().lower()


if action in ('y', 'yes'):
    for file in result:
       os.remove(file)
    print("Deleted")

else:
    print("Script ends")
