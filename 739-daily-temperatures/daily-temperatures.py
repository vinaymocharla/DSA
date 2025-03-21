class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output= [0]* len(temperatures)

        stack=[]   #indexes


        for i,n in enumerate(temperatures):

            while stack and temperatures[stack[-1]]<n:

                stackIndex= stack.pop()

                output[stackIndex]=i-stackIndex

            stack.append(i)
        
        return output