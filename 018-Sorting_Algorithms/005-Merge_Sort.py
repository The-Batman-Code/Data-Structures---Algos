import math


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList


# TC and SC of the above method is O(n^2) and O(1)


def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numberofBuckets / maxValue)
        arr[index_b - 1].append(j)

    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0

    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


# TC and SC of the above method is O(n^2) and O(n)


def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l + i]

    for j in range(0, n2):
        R[j] = customList[m + 1 + j]
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1


def mergeSort(customList, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)  # TC of this and above code line is O(nlogn)
        merge(customList, l, m, r)  # TC is O(n)
    return customList


# TC of the above method is O(nlogn) and SC is O(n)

clist = [6, 3, 9, 5, 7, 1, 10, 15]
print(mergeSort(clist, 0, 7))
