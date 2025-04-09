class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []
        ans=0

        for i in tokens:

            if i=='+' or i=='-' or i=='*' or i=='/':

                one = int(stack.pop())
                two = int(stack.pop())

               
                if i=='+':

                    stack.append(one+two)
                    
                    
                elif i=='-':

                    stack.append(two-one)
                    

                elif i=='*':
                    stack.append(one*two)
                    
                    

                else:

                    stack.append(int((two/one)))
                    print(stack[-1])
                    

            else:
                stack.append(i)

        if stack:
            return int(stack[-1])




        