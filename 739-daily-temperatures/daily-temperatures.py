class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res =[0]*len(temperatures)
        stack=[]     # indexes

        for i,n in enumerate(temperatures):

            while stack and temperatures[stack[-1]]<n:

                stackI = stack.pop()

                res[stackI] = i-stackI

            stack.append(i)
        return res


