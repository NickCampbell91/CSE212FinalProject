"""
Find the intersection of two given sets.
"""

def Intersection(list1, list2):
    return set(list1).intersection(list2)

list1 = [8, 6, 7, 5, 3, 0, 9]
list2 = [1, 2, 3, 4, 5, 6, 7]
print(Intersection(list1, list2))#{3, 5, 6, 7}