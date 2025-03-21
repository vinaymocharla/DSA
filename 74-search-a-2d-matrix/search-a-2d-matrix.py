class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:




        l=0
        r=len(matrix)-1

        while(l<=r):

            
            m= l+(r-l)//2
           

            if target< matrix[m][0]:

                r=m-1

            elif target > matrix[m][-1]:

                l=m+1
            else:
                

                x=0
                y=len(matrix[m])-1

                while(x<=y):

                    mm = x+(y-x)//2

                    if matrix[m][mm] == target:
                        return True
                    elif matrix[m][mm] > target:

                        y=mm-1
                    else:
                        x=mm+1

                return False
        return False