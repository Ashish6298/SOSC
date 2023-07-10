def print_pattern(rows):
    letter = ord('A')
    for i in range(1, rows + 1):
        for j in range(i):
            print(chr(letter), end=" ")
            letter += 1
        print()

print_pattern(5)
