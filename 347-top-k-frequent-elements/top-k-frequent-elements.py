class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums)+1)]

        map ={}

        res=[]*len(nums)

        for num in nums:

            map[num] = 1 + map.get(num,0)

        for key,value in map.items():

            freq[value].append(key)

        
        for i in range(len(freq)-1,0,-1):

            for j in freq[i]:

                res.append(j)

                if(len(res)==k):
                    return res

        


        