class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        closeToParam = {')':'(', '}':'{',']':'['}

        for c in s:

            if c in closeToParam:
                if stack and stack[-1]==closeToParam[c]:
                    stack.pop()
                else:
                    return False
                
                

            else:

                stack.append(c)

        return True if not stack else False


            

    
        