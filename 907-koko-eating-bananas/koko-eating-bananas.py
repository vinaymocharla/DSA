class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l=1

        r= max(piles)
        res= 0

        while(l<=r):

            k=l+(r-l)//2

            hours=0

            for i in piles:

                hours += math.ceil(i/k)

            if hours<=h:

                res=k

                r=k-1


            else:
                l=k+1
        return res





        