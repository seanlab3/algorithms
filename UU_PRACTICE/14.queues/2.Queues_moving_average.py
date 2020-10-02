# Given a stream of integers and a window size,
# calculate the moving average of all integers in the sliding window.

from algorithms.queues.moving_average import MovingAverage

m = MovingAverage(3)

print(m.next(1))

print(m.next(10))

print(m.next(3))

print(m.next(5))

# assert m.next(1) == 1
# assert m.next(10) == (1 + 10) / 2
# assert m.next(3) == (1 + 10 + 3) / 3
# assert m.next(5) == (10 + 3 + 5) / 3

