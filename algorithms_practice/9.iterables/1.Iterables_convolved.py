"""Iterable to get every convolution window per loop iteration.
## Example Usage
```
from algorithms.iterables import convolved
# This would also work: from conv import convolved
some_list = [1, 2, 3]
for kernel_hover in convolved(some_list, kernel_size=2, stride=1, padding=2, default_value=42):
    print(kernel_hover)
```
## Result:
```
[42, 42]
[42, 1]
[1, 2]
[2, 3]
[3, 42]
[42, 42]
```
"""
from algorithms.iterables import convolved

some_list = [1, 2, 3, 4]
for kernel_hover in convolved(some_list, kernel_size=2 ,stride=1, padding=2, default_value=42):
    print(kernel_hover)

for kernel_hover in convolved(some_list, kernel_size=2 ):
    print(kernel_hover)