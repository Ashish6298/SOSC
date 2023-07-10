def print_pattern(rows):
    number = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(number, end=" ")
            number += 1
        print()

print_pattern(4)
