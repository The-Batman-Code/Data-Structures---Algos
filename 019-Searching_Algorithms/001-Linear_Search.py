def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


# TC and SC of the above method is O(n) and O(1) resp

print(linearSearch([20, 40, 30, 50, 90], 90))
