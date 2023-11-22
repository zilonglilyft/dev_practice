"""
https://leetcode.com/problems/valid-anagram/
"""
def isAnagram(s: str, t: str) -> bool:
    dict1, dict2 = {}, {}
    for char in s:
        dict1[char] = dict1.get(char, 0) + 1 # write like this, you wont need to judge if the key is existing
    for char in t:
        dict2[char] = dict2.get(char, 0) + 1
    return dict1 == dict2
# complexity: o(n)
# there is another approach with regular sort and the complexity is o(n*log(n))
"""
def isAnagram(s: str, t: str) -> bool:
    return sorted(list(s)) == sorted(list(j))
"""