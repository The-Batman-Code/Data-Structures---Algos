from array import *

# 1. Create an array and traverse
print("\nStep-1")

my_array = array("i", [1, 2, 3, 4, 5, 6])  # ------ TC = O(n) and SC = O(n)
for i in my_array:  # ------O(n)
    print(i)
# Total TC = O(n) and space complexity = O(n) as no extra space is required


# 2. Access individual elements through indexes
print("\nStep-2")


def access_element(array, index):  # TC = O(1) and SC = O(1)
    if index >= len(array):
        print("The index is greater than the length of the array")
    else:
        print(array[index])
    return -1


access_element(my_array, 6)

# 3. Append any value to the array using append() method
print("\nStep-3")

my_array.append(10)  # TC = O(1) and SC = O(1)

print(my_array)

# 4. Insert any value to the array using insert() method
print("\nStep-4")

my_array.insert(0, 99)  # TC = O(n) and SC = O(1)
print(my_array)

# 5. Extend python array using extend() method
print("\nStep-5")

my_array1 = array(
    "i", [78, 45, 67]
)  #  TC = O(k) and SC = O(k) where k is the size of the array the is being inserted
my_array.extend(my_array1)
print(my_array)

# 6. Add items from list into array using fromlist() method
print("\nStep-6")
templist = [20, 24, 35]
my_array.fromlist(
    templist
)  #  TC = O(k) and SC = O(k) where k is the size of the array the is being inserted
print(my_array)

# 7. Remove any array element using the remove() method
print("\nStep-7")

my_array.remove(
    24
)  # TC is O(n) as is has to traverse the entire array to find the element and then reindex the left elements SC is O(1)
print(my_array)

# 8. Remove last array element using the pop() method
print("\nStep-8")

my_array.pop()  # TC is O(1) and SC is O(1)
print(my_array)

# 9. Fetch any element's index using index() method
print("\nStep-9")

print(
    my_array.index(20)
)  # TC is O(n) as it has to traverse the whole array to look for the element. SC is O(1) as no extra space is needed

# 10. Reverse the array using reverse() method
print("\nStep-10")
my_array.reverse()  # TC is O(n) as it needs to scan through the entire list and reverse the order. SC = O(1) as it modifies array inplace
print(my_array)

# 11. Get array buffer info through buffer_info() method
print("\nStep-11")

print(my_array.buffer_info())

# 12. Check for  number of elements of an element using count method()
print("\nStep-12")

print(
    my_array.count(20)
)  # TC is O(n) as it goes through the entire array to get the count. SC is O(1) as no extra space is required

# 13. Convert array to a python list using tolist() method
print("\nStep-13")

print(my_array.tolist())

# 14. Slice elements from an array
print("\nStep-14")

print(my_array[1:4])
