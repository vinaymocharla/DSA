class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res= [0] * len(temperatures)

        stack=[]   #[temp,index]

        for i,n in enumerate(temperatures):


            while stack and n>stack[-1][0]:

                stackT ,stackI = stack.pop()

                res[stackI] = (i - stackI)

            stack.append([n,i])
        return res
                  
        