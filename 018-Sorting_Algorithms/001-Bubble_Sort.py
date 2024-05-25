def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)


# TC and SC of the above method is O(n^2) and O(1) resp

clist = [6, 3, 9, 5, 7, 1, 0]
bubbleSort(clist)
