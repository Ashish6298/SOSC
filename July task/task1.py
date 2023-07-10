def remove_duplicates(arr):
    return list(set(arr))
input_str =input("Enter elements of the array \n")
array = list(map(int, input_str.split()))
result = remove_duplicates(array)
print("Array after removing duplicates \n", result)

