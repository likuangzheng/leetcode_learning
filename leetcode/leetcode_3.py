# Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without
# repeating characters.


# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. 
# Note that the answer must be a substring, 
# "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_recorder = {}
        max_length = 0
        length = 0
        for position, word in enumerate(s):
            if word not in word_recorder:
                length += 1                    
            else:
                max_length = max(length, max_length)
                same_distance = position - word_recorder[word]
                length = min(same_distance, length+1)
                if length == 1:
                    word_recorder = {}
            word_recorder[word] = position
        max_length = max(length, max_length)
        return max_length

solution = Solution()
print(solution.lengthOfLongestSubstring('abcabcbb'))
print(solution.lengthOfLongestSubstring('bbbbb'))
print(solution.lengthOfLongestSubstring('pwwkew'))
print(solution.lengthOfLongestSubstring('aab'))
print(solution.lengthOfLongestSubstring('dvdf'))
print(solution.lengthOfLongestSubstring('abba'))
print(solution.lengthOfLongestSubstring('wobgrovw'))

