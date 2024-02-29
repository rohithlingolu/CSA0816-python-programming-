def remove_duplicates(sorted_array):
    if not sorted_array:
        return []

    unique_array = [sorted_array[0]]

    for i in range(1, len(sorted_array)):
        if sorted_array[i] != sorted_array[i - 1]:
            unique_array.append(sorted_array[i])

    return unique_array

# Input
sorted_array = [1, 1, 2, 2, 3, 4, 4, 5, 5]

# Output
result = remove_duplicates(sorted_array)
print(f"The array after removing duplicates: {result}")
