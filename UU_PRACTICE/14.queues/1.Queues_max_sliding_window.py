"""
Given an array and a number k
Find the max elements of each of its sub-arrays of length k.
Keep indexes of good candidates in deque d.
The indexes in d are from the current window, they're increasing,
and their corresponding nums are decreasing.
Then the first deque element is the index of the largest window value.
For each index i:
1. Pop (from the end) indexes of smaller elements (they'll be useless).
2. Append the current index.
3. Pop (from the front) the index i - k, if it's still in the deque
   (it falls out of the window).
4. If our window has reached size k,
   append the current window maximum to the output.
"""

##https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/



from algorithms.queues import max_sliding_window
a=[1, 2, 3, 1, 4, 5, 2, 3, 6]

k=3

b=[8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
l=4

print(max_sliding_window(a,k))

print(max_sliding_window(b,l))
