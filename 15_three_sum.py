def threeSum(nums):
    if len(nums) < 3:
        return []

    nums.sort()
    triplets = []

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        target = -num
        l = i + 1
        r = len(nums) - 1

        while l < r:
            sum = nums[l] + nums[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                triplets.append([num, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                r -= 1
                while nums[r] == nums[r + 1] and l < r:
                    r -= 1
    return triplets


# print(threeSum([-1, 0, 1, 2, -1, -4]))
# print(threeSum([]))
# print(threeSum([0]))
print(threeSum([-2, 0, 1, 1, 2]))
