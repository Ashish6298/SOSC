def print_pattern(rows):
    for i in range(1, rows + 1):
        if i % 2 == 0:
            print(" " * (i - 1) + "* " * (rows - i + 1))
        else:
            print(" " * (i - 1) + "* " * i)

print_pattern(3)
