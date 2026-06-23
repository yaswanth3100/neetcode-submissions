class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set={}
        if(len(s)==1):
            return 1
        maxi = 0
        start =0
        end = 0
        for i in range(0,len(s)):
            if s[i] in c_set  and c_set[s[i]] >= start:
                start = c_set.get(s[i])+1
            c_set[s[i]]=i
            maxi = max(maxi,i-start+1)
        return maxi



