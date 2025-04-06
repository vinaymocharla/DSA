class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        freqset= set()

        l=0
        r=0

        maxwindow = 0

        while(r!=len(s)):

            while(s[r] in freqset):

                freqset.remove(s[l])
                l+=1

            freqset.add(s[r])

            maxwindow = max(maxwindow, (r-l+1))

            r+=1

        return maxwindow