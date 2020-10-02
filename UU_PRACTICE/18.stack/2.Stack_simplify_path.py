"""
Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
* Did you consider the case where path = "/../"?
    In this case, you should return "/".
* Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".
"""
from algorithms.stack import simplify_path

path = "/home/"
path2 = "/a/./b/../../c/"

print(simplify_path(path))

print(simplify_path(path2))
