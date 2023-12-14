mylist = [1, 2, 3, 4]
print(mylist)

mylist.insert(2, 89)  # TC is O(n) and SC is O(1)
print(mylist)

mylist.append(78)  # TC is O(1) and SC is O(1)
print(mylist)

newlist = [56, 78, 34]  # TC is O(k) and SC is also O(k)
mylist.extend(newlist)
print(mylist)
