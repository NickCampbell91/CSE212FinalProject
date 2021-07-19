"""
Find the union of two given sets.
"""

def Union(list1, list2):
    return set(list1).union(list2)

list1 = [8, 6, 7, 5, 3, 0, 9]
list2 = [1, 2, 3, 4, 5, 6, 7]
print(Union(list1, list2))#{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#list1 provided by Jenny then distributed by Tommy Tutone