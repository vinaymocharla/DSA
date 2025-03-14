class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:


        out = set()

        nums.sort()

        for i in range(len(nums)-3):

            for j in range(i+1, len(nums)-2):

                k=j+1
                l = len(nums)-1

                while(k<l):

                    sum = nums[i]+nums[j]+nums[k]+nums[l]

                    if sum==target:

                        out.add((nums[i],nums[j],nums[k],nums[l]))

                        k+=1
                        l-=1

                    elif sum>target:

                        l-=1
                    else:
                        k+=1
        return list(out)
        