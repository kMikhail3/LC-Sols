class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort but use count of each frequency as key and use list of integers as value
        count = {}
        freq = [[] for i in range(len(nums)+1)] #list comprehension
        
        for n in nums: 
            count[n] = 1 + count.get(n, 0) #second arg = 0 to prevent crash if no existing count
        for n, cnt in count.items():
            freq[cnt].append(n)

        res = []
        for i in range(len(freq) -1,0,-1): #(start,stop,step)
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            