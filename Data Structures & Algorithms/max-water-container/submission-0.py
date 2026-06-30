class Solution:
    def maxArea(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1
        max_val = 0
        while left < right:

            area = min(nums[left], nums[right]) * (right - left)
            max_val = max(max_val, area)

            if (nums[left] > nums[right]):
                right -= 1
            else:
                left += 1

        return max_val


        