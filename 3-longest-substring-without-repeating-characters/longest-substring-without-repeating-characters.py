class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        myset= set()

        maxi=0

        l,r=0,0

        while(r!=len(s)):

            while s[r] in myset:
                myset.remove(s[l])
                l+=1

            myset.add(s[r])

            maxi=max(maxi, r-l+1)

            r+=1

        return maxi
        