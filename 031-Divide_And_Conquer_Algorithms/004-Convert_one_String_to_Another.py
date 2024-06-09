def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1 + 1, index2 + 1)
    else:
        deleteOP = 1 + findMinOperation(s1, s2, index1, index2 + 1)
        insertOP = 1 + findMinOperation(s1, s2, index1 + 1, index2)
        replaceOP = 1 + findMinOperation(s1, s2, index1 + 1, index2 + 1)
        return min(deleteOP, insertOP, replaceOP)


print(findMinOperation("table", "tbrltt", 0, 0))
