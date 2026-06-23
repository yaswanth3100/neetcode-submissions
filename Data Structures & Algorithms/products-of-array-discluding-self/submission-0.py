class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums1 = [1] * n
        nums2 = [1] * n
        ans = [1] * n
        for i in range(len(nums)):
            if (i==0):
                nums1[i]=1
            else:
                nums1[i] = nums1[i-1] * nums[i-1]
        
        n = len(nums) -1 
        while (n>=0):
            if n == len(nums) -1 :
                nums2[n] = 1
            else:
                nums2[n]= nums[n+1]* nums2[n+1]
            n= n-1

        for i in range(len(nums)):
            ans[i] = nums1[i]*nums2[i]
        
        return ans

        

