def smaller_numbers_than_current(nums):
    result = []
    for i in range(len(nums)):
        count = sum(1 for j in nums if j < nums[i])
        result.append(count)
    return result

# Test Cases
print(smaller_numbers_than_current([8,1,2,2,3]))  # Output: [4,0,1,1,3]
print(smaller_numbers_than_current([6,5,4,8]))    # Output: [2,1,0,3]
print(smaller_numbers_than_current([7,7,7,7]))    # Output: [0,0,0,0]
print(smaller_numbers_than_current([1,2,3,5,5,6])) # Output: [0,1,2,4,4,5]
print(smaller_numbers_than_current([0,0,0,0]))    # Output: [0,0,0,0]
