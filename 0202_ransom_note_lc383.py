# https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # the problem wants us to return a boolean if a ransom note can
        # be constructed from a magazine. So what do we do?

        # we maintain character counts of both ransom note, and magazine
        # using hashmaps/dictionaries
        rNote_counts = {}
        magazine_counts = {}

        # maintain character frequencies
        for char in ransomNote:
            rNote_counts[char] = rNote_counts.get(char, 0) + 1

        for char in magazine:
            magazine_counts[char] = magazine_counts.get(char, 0) + 1

        # now, if any character in ransom note doesn't exist in the magazine
        # or if that character is used more than the times present in the magazine
        # we can just return false
        for char in rNote_counts:
            if char not in magazine_counts or magazine_counts[char] < rNote_counts[char]:
                return False

        # otherwise, True, we can construct the ransome note
        return True

        # time complexity: O(n)
        # space complexity: O(n)

        # n is limited to 26 (alphabets)
        # we can also just maintain arrays of size 26, and use ord() to
        # convert character to ascii value for indexing.


# ps: i love hashmap problems :)
