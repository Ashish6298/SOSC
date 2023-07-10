def replace_first_vowel(string):
    vowels = 'aeiouAEIOU'
    for char in string:
        if char in vowels:
            return string.replace(char, '-', 1)
    return string
input_str = input("Enter the string\n")
result = replace_first_vowel(input_str)
print("After removing the vowels new string is\n", result)
