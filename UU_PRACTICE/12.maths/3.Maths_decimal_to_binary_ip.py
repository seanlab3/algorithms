"""
Given an ip address in dotted-decimal representation, determine the
binary representation. For example,
decimal_to_binary(255.0.0.5) returns 11111111.00000000.00000000.00000101
accepts string
returns string
"""

from algorithms.maths import decimal_to_binary_util,decimal_to_binary_ip

ip="192.168.30.9"

print(decimal_to_binary_ip(ip))