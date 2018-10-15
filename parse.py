import sys

# FIND ONES WITH PORT 80 OPEN
num_lines = sum(1 for line in open('scans/tcpack.scan'))

print(num_lines)
