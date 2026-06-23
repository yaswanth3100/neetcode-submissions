class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for i in s:
            if i in map:
                map[i] = 1 + map[i]
            else:
                map[i] = 1

        map1 = {}
        for i in t:
            if i not in map:
                return False

            if i in map1:
                map1[i] = 1 + map1[i]
            else:
                map1[i] = 1
        
        return map1 == map
            
            
            