# leetcode 3
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        slideWindow = set()
        left, maxLength = 0, 0
        for right in range(len(s)):
            while s[right] in slideWindow: 
                slideWindow.remove(s[left])
                left += 1
            slideWindow.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength

'''
Why choose set() as data structure to store the slide window?
It is because we need to tell if a character is in the slide window quickly. 
From Time Complexity perspective, it is much better. With list to tell if an element is in the slide window or to remove an element from the slide window, the Time Complexity is O(n); while using set, it is O(1). Overall Time Complexity comparison between List vs Set is O(n*n) vs O(n)

If using dict, there is additional Space occupancy as there is no need to save the Character to Index mapping. 
'''
