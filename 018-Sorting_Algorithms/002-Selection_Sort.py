def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i + 1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)


# TC and SC of the above method is O(n^2) and O(1)

clist = [6, 3, 9, 5, 7, 1, 0]
selectionSort(clist)
