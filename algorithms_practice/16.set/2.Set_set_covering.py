"""
Universe *U* of n elements
Collection of subsets of U:
    S = S1,S2...,Sm
    Where every substet Si has an associated cost.
Find a minimum cost subcollection of S that covers all elements of U
Example:
    U = {1,2,3,4,5}
    S = {S1,S2,S3}
    S1 = {4,1,3},    Cost(S1) = 5
    S2 = {2,5},      Cost(S2) = 10
    S3 = {1,4,3,2},  Cost(S3) = 3
    Output:
        Set cover = {S2, S3}
        Min Cost = 13
"""
from algorithms.set.set_covering import optimal_set_cover,greedy_set_cover



universe = {1, 2, 3, 4, 5}
subsets = {'S1': {4, 1, 3}, 'S2': {2, 5}, 'S3': {1, 4, 3, 2}}
costs = {'S1': 5, 'S2': 10, 'S3': 3}

optimal_cover = optimal_set_cover(universe, subsets, costs)
optimal_cost = sum(costs[s] for s in optimal_cover)

greedy_cover = greedy_set_cover(universe, subsets, costs)
greedy_cost = sum(costs[s] for s in greedy_cover)

print('Optimal Set Cover:')
print(optimal_cover)
print('Cost = %s' % optimal_cost)

print('Greedy Set Cover:')
print(greedy_cover)
print('Cost = %s' % greedy_cost)