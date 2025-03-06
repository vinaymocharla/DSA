class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        output = set(nums)

        longest=0

        for i in output:

            if (i-1) not in output:

                length=0

                while length+i in output:
                    length+=1

                longest= max(longest,length)

        return longest

                