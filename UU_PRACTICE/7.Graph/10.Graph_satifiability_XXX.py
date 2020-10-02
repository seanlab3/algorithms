'''
Given a formula in conjunctive normal form (2-CNF), finds a way to assign
True/False values to all variables to satisfy all clauses, or reports there
is no solution.
https://en.wikipedia.org/wiki/2-satisfiability
'''

## XXX

from algorithms.graph.satisfiability import *

formula = [(('x', False), ('y', False)),
           (('y', True), ('y', True)),
           (('a', False), ('b', False)),
           (('a', True), ('c', True)),
           (('c', False), ('b', True))]
result = solve_sat(formula)

for (variable, assign) in result.items():
    print("{}:{}".format(variable, assign))