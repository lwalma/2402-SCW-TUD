"""
Aim:  this script counts the number of lines in standard input
Input: Strings from the command line
Output: the lines in a standard input
Author: L. Walma
"""

import sys


count = 0
for line in sys.stdin:
    count += 1


print(count, "lines in standard input")
