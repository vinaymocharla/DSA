class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l=1
        r=max(piles)

        res=r

        while(l<=r):

            m = l+(r-l)//2

            ans=0

            for p in piles:

                ans+=  math.ceil(p/m)

            if ans<=h:

                r=m-1

                res=m
            else:
                l=m+1

        return res




        