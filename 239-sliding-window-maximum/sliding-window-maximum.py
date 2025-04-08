class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        mydeque= deque()

        r=0

        ans=[]

        while(r!=len(nums)):

            if mydeque and mydeque[0] < r-k+1:

                mydeque.popleft()

            while mydeque and nums[r]> nums[mydeque[-1]]:

                mydeque.pop()

            mydeque.append(r)

            if r>=k-1:

                ans.append(nums[mydeque[0]])

            r+=1

        return ans

            


        