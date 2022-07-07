class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def partition(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[r] = pivot, nums[p]

            if p > k:
                return partition(l, p - 1)
            elif p < k:
                return partition(p + 1, r)
            else:
                return nums[p]

        return partition(0, len(nums) - 1)
