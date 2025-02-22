class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        output=set()


        for i in range(len(nums)-2):

            if i>0 and nums[i]==nums[i-1]:
                continue

            j=i+1
            k=len(nums)-1

            while(j<k):

                curr_sum = nums[i]+nums[j]+nums[k]

                if(curr_sum>0):
                    k-=1
                elif(curr_sum<0):
                    j+=1

                else:

                    output.add((nums[i],nums[j],nums[k]))

                    j+=1
                    k-=1

                    while(j<k and nums[j]==nums[j-1]): j+=1
                    while(j<k and nums[k]==nums[k+1]): k-=1
                    
        return list(output)

        