
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
        
#        longest_length = [0]
#        def findLength(purpose_string, length, word_cache):
#            
#            print(purpose_string, length, word_cache)
#            if not purpose_string:
#                if length > longest_length[0]:
#                    longest_length[0] = length
#                return length
#
#            if purpose_string[0] in word_cache:
#                if length > longest_length[0]:
#                    longest_length[0] = length
#                return findLength(purpose_string, 0, [])
#            else:
#                length += 1
#                word_cache.append(purpose_string[0])
#
#           return findLength(purpose_string[1:], length, word_cache)
#
#       findLength(s, 0, [])
#        return longest_length[0]

solution = Solution()
print(solution.lengthOfLongestSubstring('abcabcbb'))
print(solution.lengthOfLongestSubstring('bbbbb'))
print(solution.lengthOfLongestSubstring('pwwkew'))
print(solution.lengthOfLongestSubstring('aab'))
print(solution.lengthOfLongestSubstring('dvdf'))
print(solution.lengthOfLongestSubstring('abba'))
print(solution.lengthOfLongestSubstring('wobgrovw'))

