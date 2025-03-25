class Solution:
    def findMin(self, nums: List[int]) -> int:


        l=0

        r=len(nums)-1

        res=nums[0]

        while(l<=r):


            

            if nums[l]<nums[r]:

                res=min(res,nums[l])
                break
            
            m= l+(r-l)//2

            if nums[m] >= nums[l]:

                res= min(res,nums[l])

                l=m+1
            else:

                r=m
        return res




        