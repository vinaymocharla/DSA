class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:



        nums.sort()
        out=set()


        for i in range(len(nums)-3):

            if i>0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,len(nums)-2):

                k=j+1

                l=len(nums)-1


                while(k<l):

                    sum = nums[i]+nums[j]+nums[k]+nums[l]

                    if sum > target:

                        l-=1
                    elif sum< target:

                        k+=1
                    else:

                        out.add((nums[i],nums[j],nums[k],nums[l]))

                        k+=1
                        l-=1

        return list(out)



        