class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        out = set()

        nums.sort()

        for i in range(len(nums)-2):

            if i>0 and nums[i]==nums[i-1]:i+=1

            j=i+1
            k=len(nums)-1

            while(j<k):

                sum = nums[i]+nums[j]+nums[k]

                if sum>0:
                    k-=1
                elif sum<0:
                    j+=1
                else:

                    out.add((nums[i],nums[j],nums[k]))

                    j+=1
                    k-=1

        return list(out)


        