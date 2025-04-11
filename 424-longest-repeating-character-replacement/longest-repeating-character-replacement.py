class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}

        l=0
        r=0

        maxoccur = 0
        out=0

        while(r!=len(s)):

            freq[s[r]] = freq.get(s[r],0)+1

            maxoccur = max(maxoccur, freq.get(s[r]))

            while((r-l+1)-maxoccur > k):
                freq[s[l]] -=1

                l+=1



            if ((r-l+1)-maxoccur <=k):

                out= max(out,(r-l+1))

        

                

            r+=1

        return out






        