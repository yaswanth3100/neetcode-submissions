class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [0]*(n+1)
        for i in range(n+1):
            if(i<=3):
                nums[i] = i
            else:
                nums[i] = nums[i-1]+nums[i-2]
        return nums[n]

        
        




