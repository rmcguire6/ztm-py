def mergeTwoSorted(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    mergedList = []
    index1 = 0
    index2 = 0
    while ((index1 < len(list1)) or (index2 < len(list2))):
        if (list1[index1] < list2[index2]):
            mergedList.append(list2[index2])
            index2 = index2 + 1
        else:
            mergedList.append(list1[index2])
            index1 = index1 + 1
    return mergedList
print(mergeTwoSorted([0], []))
print(mergeTwoSorted([], [2]))
print(mergeTwoSorted([0,2], [0]))
# print(mergeTwoSorted([0,3,4,31], [4,6,30]))
