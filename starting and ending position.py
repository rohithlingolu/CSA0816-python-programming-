def searchRange(nums, target):
    def binary_search_left(nums, target):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    def binary_search_right(nums, target):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    left_index = binary_search_left(nums, target)
    right_index = binary_search_right(nums, target)

    return [left_index, right_index]

nums = [5, 7, 7, 8, 8, 10]
target = 8
result = searchRange(nums, target)
print("Starting and ending position of", target, ":", result)
