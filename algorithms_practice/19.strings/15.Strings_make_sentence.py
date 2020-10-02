"""
For a given string and dictionary, how many sentences can you make from the
string, such that all the words are contained in the dictionary.
eg: for given string -> "appletablet"
"apple", "tablet"
"applet", "able", "t"
"apple", "table", "t"
"app", "let", "able", "t"
"applet", {app, let, apple, t, applet} => 3
"thing", {"thing"} -> 1
"""
from algorithms.strings import make_sentence
s="appletablet"

d={"app", "let", "apple", "t", "applet"}

print(make_sentence(s,d))
