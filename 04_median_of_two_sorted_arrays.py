def findMedianSortedArrays(nums1, nums2):
    merged_array = nums1 + nums2
    merged_array.sort()

    arr_len = len(merged_array)
    if arr_len % 2 == 0:
        return (
            merged_array[(arr_len - 1) // 2] + merged_array[(arr_len - 1) // 2 + 1]
        ) / 2
    return merged_array[(arr_len - 1) // 2]


nums1 = [1, 2]
nums2 = [3, 4]

print(findMedianSortedArrays(nums1, nums2))
