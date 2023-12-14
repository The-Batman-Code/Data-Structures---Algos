mylist = [1, 2, 3, 4, 5, 6, 7, 8]
print(mylist)

mylist[0:2] = ["b", "d"]  # TC is O(k) and SC is O(1)
print(mylist)

mylist.pop(
    0
)  # TC is O(n) as it shifts the elements one index to the left and SC is O(1)
print(mylist)

print(mylist.pop(5))

mylist.pop()
print(mylist)

del mylist[
    2
]  # TC is O(n) as it shifts the elements one index to the left and SC is O(1)
print(mylist)

mylist.remove(
    "b"
)  # TC is O(n) as it shifts the elements one index to the left and SC is O(1)
print(mylist)
