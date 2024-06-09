# Top Down Approach
def numberFactorTD(n, tempDict):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in tempDict:
            p1 = numberFactorTD(n - 1, tempDict)
            p2 = numberFactorTD(n - 3, tempDict)
            p3 = numberFactorTD(n - 4, tempDict)
            tempDict[n] = p1 + p2 + p3
        return tempDict[n]


print(numberFactorTD(5, {}))


# Bottom Up Approach
def numberFactorBU(n):
    tempArr = [1, 1, 1, 2]
    for i in range(4, n + 1):
        tempArr.append(tempArr[i - 1] + tempArr[i - 3] + tempArr[i - 4])
    return tempArr[n]


print(numberFactorBU(5))
