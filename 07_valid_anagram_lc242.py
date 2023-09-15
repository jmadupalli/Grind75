# https://leetcode.com/problems/valid-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # maintain a dictionary for frequency of characters
        counts_s = {}
        counts_t = {}

        for c in s:
            counts_s[c] = 1 + counts_s.get(c, 0)
        for c in t:
            counts_t[c] = 1 + counts_t.get(c, 0)
        # if the frequences match, they are anagrams :)
        # in python3 dictionaries are ordered, so you can be sure this will work.
        return counts_s == counts_t

        # time complexity: O(n)
        # space complexity: O(n)
