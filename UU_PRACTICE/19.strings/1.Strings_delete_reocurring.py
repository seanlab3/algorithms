"""
QUESTION: Given a string as your input, delete any reoccurring
character, and return the new string.
This is a Google warmup interview question that was asked duirng phone screening
at my university.
"""

from algorithms.strings.delete_reoccurring import delete_reoccurring_characters

a="abbbcad"

print(delete_reoccurring_characters(a))