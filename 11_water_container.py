from turtle import left


def maxArea(height):
    left_idx = 0
    right_idx = len(height) - 1

    max_area = (right_idx - left_idx) * min(height[left_idx], height[right_idx])
    print(max_area)
    while left_idx < right_idx:
        # area_tmp = (right_idx - left_idx) * min(height[left_idx], height[right_idx])
        # max_area = max(area_tmp, max_area)

        # updejtamo levega, ELSE updejtamo desnega
        if height[left_idx] <= height[right_idx]:
            for i in range(left_idx + 1, len(height)):
                if height[i] > height[left_idx]:
                    left_idx = i
                    break
                if i >= right_idx:
                    return max_area
            else:
                return max_area
        else:
            for i in range(right_idx - 1, 0, -1):
                if height[i] > height[right_idx]:
                    right_idx = i
                    break
                if i <= left_idx:
                    return max_area
            else:
                return max_area

        max_area = max(
            max_area, (right_idx - left_idx) * min(height[left_idx], height[right_idx])
        )
        # updejtamo left_idx in right_idx
        # for i in range(left_idx + 1, len(height)):
        #     if height[i] > height[left_idx]:
        #         left_idx = i
        #         break
        #     if i >= right_idx:
        #         return max_area

        # area_tmp = (right_idx - left_idx) * min(height[left_idx], height[right_idx])
        # max_area = max(area_tmp, max_area)

        # for i in range(right_idx - 1, 0, -1):
        #     if height[i] > height[right_idx]:
        #         right_idx = i
        #         break
        #     if i <= left_idx:
        #         return max_area

        # area_tmp = (right_idx - left_idx) * min(height[left_idx], height[right_idx])
        # max_area = max(area_tmp, max_area)

    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))

x = [2, 1]
print(maxArea(x))
