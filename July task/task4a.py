def DecimalToOctal(decimal_num):
    octal_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_num = str(remainder) + octal_num
        decimal_num //= 8
    return octal_num
decimal_input = int(input("Enter the decimal number\n"))
octal_output = DecimalToOctal(decimal_input)
print("Octal number is\n", octal_output)
