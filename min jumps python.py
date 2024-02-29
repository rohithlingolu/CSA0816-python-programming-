def min_jumps(arr):
    n = len(arr)
    if n == 0 or arr[0] == 0:
        return -1
    
    jumps = 1
    current_max = arr[0]
    steps = arr[0]

    for i in range(1, n):
        if i == n - 1:
            return jumps
        
        current_max = max(current_max, i + arr[i])
        steps -= 1
        
        if steps == 0:
            jumps += 1
            if i >= current_max:
                return -1
            steps = current_max - i

# Test Cases
print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])) # Output: 3
print(min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) # Output: 10
print(min_jumps([2, 3, 1, 1, 4]))                  # Output: 2
print(min_jumps([1, 3, 6, 1, 0, 9]))                # Output: 3
print(min_jumps([2, 3, 0, 1, 4]))                  # Output: 2
