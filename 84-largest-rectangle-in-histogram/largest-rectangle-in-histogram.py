class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        stack=[]  # index,height

        area=0

        for i,n in enumerate(heights):

            start = i

            while stack and stack[-1][1]>n:

                index,height = stack.pop()

                area = max(area, height*(i-index))
                start=index

            
            stack.append([start,n]) 
        
        for i,n in stack:

            area = max(area, n* (len(heights)-i))
        return area


        