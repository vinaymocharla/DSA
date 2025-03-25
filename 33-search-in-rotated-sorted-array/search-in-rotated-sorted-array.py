class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums)-1

        while(l<=r):

            #left sorted array

            m=l+(r-l)//2

            if target==nums[m]:
                return m

            if nums[l]<=nums[m]:

                if target>nums[m] or target<nums[l]:
                    l=m+1
                else:
                    r=m-1


            #right sorted array
            else:

                if target<nums[m] or target>nums[r]:

                    r=m-1
                else:
                    l=m+1
        return -1
        