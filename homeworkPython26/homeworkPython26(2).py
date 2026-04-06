import os
import sys

if len(sys.argv) != 3:
    print('Expected only 3 arguments (script name, "path", file type)')
    sys.exit(1)


path = sys.argv[1]
file_type = sys.argv[2]
result = [f'Files with type "{file_type}":']


if not os.path.exists(path):
    print('Enter correct path')
    sys.exit(1)


os.chdir(path)


for root, dirs, files in os.walk(path):
    for file in files:
        if os.path.basename(file).endswith(file_type):
            result.append(os.path.join(root,file))

print('\n- '.join(result))


if not result[1:]:
    print("Not found")
    sys.exit(1)


action = input("Wanna delete? (y/n): ")


if action in ('y', 'yes'):
    for file in result[1:]:
       os.remove(os.path.abspath(file))
    else:
        print("Deleted")

else:
    print("Script end's")
