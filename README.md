# My Solutions to Option 1

Solution 1:

This solution is naive and a bit hacky, but the main approach is to sort the list and then traverse the list to find which values repeated as that will be the duplicate. The time complexity of this solutoion is O(nlogn) because that is the time complexity of pythons .sort() function, and then traversiing the list once is a time complexit of O(n) but O(n) + O(nlogn) simplifies to O(nlogn). The space complexity is O(1) because we are not using any extra space.

Solution 2:

This solution is more efficient than the first soltuion and utilizes a set. The strategy is to traverse the list and add values to the set if the value is in the set already then that value is the duplicate and we return. The time complexity is O(n) since I traverse the list only once, and the space complexity is O(n) as well as in the worst case we would have to traverse and store all N unique elements.

I believe that there is no more time-efficient solution as that would involve not traversing the entire list and I'm unsure how you could find duplicates without traversing the list, howeve there may be a more space-efficeint (O(1) for example) solution.
