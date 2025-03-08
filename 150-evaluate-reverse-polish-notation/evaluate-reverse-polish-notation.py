class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]

        if len(tokens)==1:
            return int(tokens[0])

        for i in tokens:

            if i=='+' or i=='-' or i=='*' or i=='/':

                two= int(stack.pop())
                one= int(stack.pop())
                

                if i=='+':

                    res=one+two
                elif i=='-':
                    res=one-two
                elif i=='*':
                    res=one*two
                else:
                    res=(one/two)

                stack.append(int(res))

            else:

                stack.append(i)
        print(stack)
        return stack[-1]




        