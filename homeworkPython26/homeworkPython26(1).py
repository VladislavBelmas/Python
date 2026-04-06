import os
import sys

if len(sys.argv) != 2:
    print("Enter only 1 argument")
    sys.exit(1)


path = sys.argv[1]
folders = ['Folders:']
files = ['Files:']


if not os.path.exists(path):
    print('Enter correct path')
    sys.exit(1)


os.chdir(path)


for item in os.listdir(path):

    if os.path.isfile(item):
        files.append(f'- {item}')

    elif os.path.isdir(item):
        folders.append(f'- {item}')


print('\n'.join(folders),'\n')
print('\n'.join(files))








