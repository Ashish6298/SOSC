def print_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + i), end=" ")
        print()
n = int(input("Enter the number of rows\n"))
print_pattern(n)
