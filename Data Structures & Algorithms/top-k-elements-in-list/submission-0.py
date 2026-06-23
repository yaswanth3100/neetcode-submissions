class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap + map
        map = {}
        for i in nums:
            map[i]=map.get(i,0)+1
        
            heap = []
        for key in map:
            heap.append((key, map[key]))
        heap.sort(key=lambda x: x[1])
        top_k = heap[-k:]
        ans =  [key for key, value in top_k]
        return ans

