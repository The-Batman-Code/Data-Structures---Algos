def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)


clist = [6, 3, 9, 5, 7, 1, 0]
bubbleSort(clist)
