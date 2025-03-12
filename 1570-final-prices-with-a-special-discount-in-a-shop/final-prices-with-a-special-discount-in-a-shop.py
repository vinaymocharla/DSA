class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        res= prices.copy()
        stack=[]


        for i,n in enumerate(prices):

            while stack and (prices[stack[-1]]>n or prices[stack[-1]]==n):

                stackI = stack.pop()

                res[stackI] = prices[stackI]-n

            stack.append(i)


        return res