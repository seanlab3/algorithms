
from algorithms.bit import int_to_bytes_big_endian,int_to_bytes_little_endian,bytes_big_endian_to_int,bytes_little_endian_to_int

### XXX

n=13345555
nstr="13345555"
print("int_to_bytes_big_endian")
print(int_to_bytes_big_endian(n))

print("int_to_bytes_little_endian")
print(int_to_bytes_little_endian(n))

print("bytes_big_endian_to_int")
print(bytes_big_endian_to_int(nstr))

print("bytes_little_endian_to_int")
print(bytes_little_endian_to_int(nstr))