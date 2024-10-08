# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

from typing import List

# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

# `input` contains exactly N+1 numbers
# `input` elements are integers in the domain [1, N]
# `input` contains all integers in the domain [1, N] at least once
# `findDuplicate` returns an `int`: the duplicate integer
def findDuplicate1(input: List[int]) -> int:
    input.sort()
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            return input[i]
    raise Exception("No duplicate found")

def findDuplicate2(input: List[int]) -> int:
    seen = set()
    for item in input:
        if item in seen:
            return item
        seen.add(item)
    raise Exception("No duplicate found")