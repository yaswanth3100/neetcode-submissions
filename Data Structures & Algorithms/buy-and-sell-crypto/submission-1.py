class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        min = 1000
        min_index = 0
        ans =0
        for i in range(0,len(nums)):
            if(min > nums[i]):
                min = nums[i]
                min_index = i
            else:
                ans = max(ans, nums[i]-nums[min_index])        
        return ans

            

        
