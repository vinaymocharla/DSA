class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        myset= set()

        l=0
        r=0

        ans=0

        while(r!=len(s)):

            while s[r] in myset:

                myset.remove(s[l])
                l+=1

            myset.add(s[r])
            ans=max(ans,(r-l+1))
            r+=1
        return ans
        