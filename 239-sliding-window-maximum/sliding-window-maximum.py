class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans=[]

        mydeque = deque()


      #  l=0
        r=0

        while(r!=len(nums)):

            if mydeque and mydeque[0] < r-k+1:

                mydeque.popleft()

            while(mydeque and nums[r]>nums[mydeque[-1]]):

                mydeque.pop()

            mydeque.append(r)

            if r>=k-1:

                ans.append(nums[mydeque[0]])

            r+=1

        return ans

            



            




        