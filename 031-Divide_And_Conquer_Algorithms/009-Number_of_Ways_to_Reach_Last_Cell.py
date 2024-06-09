def numberofPaths(twoArray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twoArray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return numberofPaths(twoArray, 0, col - 1, cost - twoArray[row][col])
    elif col == 0:
        return numberofPaths(twoArray, row - 1, 0, cost - twoArray[row][col])
    else:
        op1 = numberofPaths(twoArray, row - 1, col, cost - twoArray[row][col])
        op2 = numberofPaths(twoArray, row, col - 1, cost - twoArray[row][col])
        return op1 + op2


TwoDList = [[4, 7, 1, 6], [5, 7, 3, 9], [3, 2, 1, 2], [7, 1, 6, 3]]

print(numberofPaths(TwoDList, 3, 3, 25))
