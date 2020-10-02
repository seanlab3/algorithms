from algorithms.bfs import ladder_length

"""

Given two words (begin_word and end_word), and a dictionary's word list,
find the length of shortest transformation sequence
from beginWord to endWord, such that:
Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,
Given:
begin_word = "hit"
end_word = "cog"
word_list = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Note:
Return -1 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.


"""

begin_word = "hit"
end_word = "cog"
word_list = ["hot","dot","dog","lot","log"]

print(ladder_length(begin_word,end_word,word_list))