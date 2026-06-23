class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for i in strs:
            ans = ''.join(sorted(i))
            if ans not in m:
                m[ans] = [i]
            else:
                m.get(ans).append(i)

        arr = []
        for i in m:
            arr.append(m[i])
        
        return arr
        