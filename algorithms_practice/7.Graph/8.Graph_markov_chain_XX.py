from algorithms.graph.markov_chain import iterating_markov_chain

## XXX

my_chain = {
    'A': {'A': 0.6,
          'E': 0.4},
    'E': {'A': 0.7,
          'E': 0.3}
}

print(iterating_markov_chain(my_chain))