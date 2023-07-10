def isPalindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]
input_str = input("Enter the string\n")
if isPalindrome(input_str):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
