class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            s.add(i)

        longest = 0 

        for i in s:

            if not i-1 in s:
                length = 1
                while(i+length in s):
                    length = length+1
                longest = max(longest, length )
        return longest




