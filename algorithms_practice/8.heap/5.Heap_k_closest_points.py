"""Given a list of points, find the k closest to the origin.
Idea: Maintain a max heap of k elements.
We can iterate through all points.
If a point p has a smaller distance to the origin than the top element of a heap, we add point p to the heap and remove the top element.
After iterating through all points, our heap contains the k closest points to the origin.
"""
"""
# Python program for implementation of  
# above approach 
  
# Function to return required answer 
def pClosest(points, K): 
  
    points.sort(key = lambda K: K[0]**2 + K[1]**2) 
  
    return points[:K] 
  
# Driver program 
points = [[3, 3], [5, -1], [-2, 4]] 
  
K = 2
  
print(pClosest(points, K)) 

"""
from algorithms.heap import k_closest
points = [[1,3],[-2,2]]
k=1

print(k_closest(points,k))