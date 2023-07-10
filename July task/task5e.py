def print_pattern(rows):
    for i in range(-rows + 1, rows):
        print(" " * abs(i) + "* " * (rows - abs(i)))

print_pattern(3)
