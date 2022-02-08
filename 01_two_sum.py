def twoSum(nums, target):
    difference = {}
    for i, num in enumerate(nums):
        if num in difference.keys():
            return [difference[num], i]
        difference[target - num] = i


nums = [3, 3]
target = 6

print(twoSum(nums, target))
