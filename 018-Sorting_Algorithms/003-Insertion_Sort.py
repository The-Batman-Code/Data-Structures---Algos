def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    print(customList)


# TC and SC of the above method is O(n^2) and O(1)

clist = [6, 3, 9, 5, 7, 1, 0]
insertionSort(clist)
