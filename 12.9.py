#Yasir Mushtaque
#1769403

parts = input().split()
name = parts[0]

while name != '-1':
    try:
        int(parts[1]) + 1
    except ValueError as exception:
        parts[1] = -1
    age = int(parts[1]) + 1

    print('{} {}'.format(name, age))

    parts = input().split()
    name = parts[0]