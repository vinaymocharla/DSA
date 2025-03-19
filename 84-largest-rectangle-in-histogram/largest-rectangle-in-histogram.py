class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if len(heights) == 1:
            return heights[0]

        stack=[]

        area=0

       

        for i,n in enumerate(heights):

            start=i

            while stack and stack[-1][1]>n:


                index,height = stack.pop()

                area = max(area, height*(i-index) )

                start = index

                

            stack.append([start,n])

        for i,h in stack:
            area = max(area, h*(len(heights)-i))

                

               
        return area
        