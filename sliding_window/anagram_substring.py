"""
Problem: Find Anagram in String

Given a string `text` and a string `pattern`, return `True` if any substring of `text` with length equal to `len(pattern)` is an anagram of `pattern`, otherwise return `False`.

Example:
Input: text = "cbaebabacd", pattern = "abc"
Output: True
Explanation: Substring "cba" (index 0-2) is an anagram of "abc" ✓

Example 2:
Input: text = "hello", pattern = "abc"
Output: False
Explanation: No substring of length 3 is an anagram of "abc"

"""

# def anagram_substring(text, pattern):
#     cur_str = ""
#     k = len(pattern)
#     for i in range(k):
#         cur_str += text[i]
#     if sorted(cur_str) == sorted(pattern):
#         return True
    
#     for i in range(len(text) - k):
#         cur_str = cur_str[1:] # this line creates a new string every single time
#         cur_str += text[i + k]
    
#         if sorted(cur_str) == sorted(pattern):
#             return True
    
#     return False

# Time complexity: O(n klogk)
# Space complexity: O(1)

# Optimized Way: Dictionaries

def anagram_substring(text, pattern):
    pattern_dict = {}
    k = len(pattern)

    # creating pattern_dict
    for i in range(k):
        if pattern[i] in pattern_dict:
            pattern_dict[pattern[i]] += 1
        else:
            pattern_dict[pattern[i]] = 1
    
    text_dict = {}

    # creating the first text_dict
    for i in range(k):
        if text[i] in text_dict:
            text_dict[text[i]] += 1
        else:
            text_dict[text[i]] = 1
    
    print(text_dict, pattern_dict)

    if text_dict == pattern_dict:
        return True
    
    # check for all possible windows
    for i in range(len(text) - k):
        if text[i] in text_dict:
            text_dict[text[i]] -= 1
            if text_dict[text[i]] == 0:
                del text_dict[text[i]]
        if text[i+k] in text_dict:
            text_dict[text[i+k]] += 1
        else:
            text_dict[text[i+k]] = 1
        
        print(text_dict, pattern_dict)
        if text_dict == pattern_dict:
            return True
    
    return False

text = "cbaebabacd"
pattern = "acd"



print(anagram_substring(text, pattern))