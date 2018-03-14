# coding:utf-8
__date__ = '2018/3/14 10:03'


"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a 
subsequence and not a substring.


"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length, start, char_dict = 0, 0, {}
        for idx, char in enumerate(s, 1):
            if char_dict.get(char, -1) >= start:
                start = char_dict[char]
            char_dict[char] = idx
            max_length = max(max_length, idx - start)
        return max_length

