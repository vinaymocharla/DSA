class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        output= set(nums)

        longest =0

        for num in output:

            if (num-1) not in output:

                length=0

                while(num+length) in output:
                    length+=1

                longest = max(length,longest)

        return longest
        