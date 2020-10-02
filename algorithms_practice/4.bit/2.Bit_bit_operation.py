"""
Fundamental bit operation:
    get_bit(num, i): get an exact bit at specific index
    set_bit(num, i): set a bit at specific index
    clear_bit(num, i): clear a bit at specific index
    update_bit(num, i, bit): update a bit at specific index
"""

"""
This function shifts 1 over by i bits, creating a value being like 0001000. By
performing an AND with num, we clear all bits other than the bit at bit i.
Finally we compare that to 0
"""

from algorithms.bit import get_bit,set_bit,clear_bit,update_bit

n=13
print("get_bit")
print(get_bit(n,3))

print("set_bit")
print(set_bit(n,2))


print("clear_bit")
print(clear_bit(n,2))


print("update_bit")
print(update_bit(n,2,3))