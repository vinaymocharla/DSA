class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        windowsum   =  sum(nums[:k])

        maxsum = windowsum


        for i in range(k,len(nums)):

            windowsum +=  nums[i] - nums[i-k]

            maxsum = max(maxsum,windowsum)

        return maxsum/k