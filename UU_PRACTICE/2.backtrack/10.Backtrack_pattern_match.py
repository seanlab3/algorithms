from algorithms.backtrack import pattern_match

"""
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
"""
pattern = "abab"
str = "redblueredblue"
print(pattern_match(pattern,str))
