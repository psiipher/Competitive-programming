'''
https://leetcode.com/problems/container-with-most-water/
'''

def maxArea(self, height: List[int]) -> int:
    if len(height) == 0 or len(height) == 1:
        return 0
    if len(height) == 2:
        return min(height)
    left = 0
    right = len(height)-1
    max_area = 0
    while left != right:
        if height[left] > height[right]:
            area = height[right] * (right - left)
            right -= 1
        else:
            area = height[left] * (right - left)
            left += 1
        if area > max_area:
            max_area = area
    return max_area
