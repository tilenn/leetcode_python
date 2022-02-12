def threeSumClosest(nums, target):
    nums.sort()
    closest_three_sum = None

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1

        while l < r:
            sum = num + nums[l] + nums[r]
            # print(sum)
            if closest_three_sum is None:
                # print("hehe")
                closest_three_sum = sum
            else:
                diff_1 = abs(closest_three_sum - target)
                diff_2 = abs(sum - target)
                # print("diff_1,", diff_1, diff_2)
                if diff_1 > diff_2:
                    closest_three_sum = sum
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                r -= 1
                while nums[r] == nums[r + 1] and l < r:
                    r -= 1
    return closest_three_sum


print(threeSumClosest([-1, 2, 1, -4], 1))
# print(threeSumClosest([0, 0, 0], 1))
