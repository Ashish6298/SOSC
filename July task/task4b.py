def DecimalToBinary(decimal_num):
    binary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    return binary_num
decimal_input = int(input("Enter a decimal number\n"))
binary_output = DecimalToBinary(decimal_input)
print(" The Binary number is \n",binary_output)
