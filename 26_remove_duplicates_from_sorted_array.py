class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        prev = nums[0]
        for element in nums:
            if element != prev:
                nums[index] = prev
                index += 1
                prev = element
        nums[index] = prev
        return index + 1
