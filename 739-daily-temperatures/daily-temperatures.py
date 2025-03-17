class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack=[]   #indexes

        output=[0]* len(temperatures)

        for i,n in enumerate(temperatures):

            while stack and temperatures[stack[-1]]<n:

                stackIndex= stack[-1]

                output[stackIndex] = i - stackIndex
                stack.pop()

            stack.append(i)


        return output

        