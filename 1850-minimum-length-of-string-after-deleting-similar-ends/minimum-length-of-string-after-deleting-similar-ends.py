class Solution:
    def minimumLength(self, s: str) -> int:

        l=0
        r=len(s)-1



        while(l<r) and s[l]==s[r]:


            char = s[l]

            while(l<=r and s[l]==char):
                l+=1
            while(r>=l and s[r]==char):
                r-=1

        return  r-l+1
        