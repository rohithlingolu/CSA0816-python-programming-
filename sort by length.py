def sort_by_length(lst):
    return sorted(lst, key=len)

my_list = ["apple", "banana", "kiwi", "orange", "pineapple"]

sorted_list = sort_by_length(my_list)

print("Original list:", my_list)
print("Sorted list by length of elements:", sorted_list)
