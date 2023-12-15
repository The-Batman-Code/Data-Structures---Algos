my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

target = 20

if (
    target in my_list
):  # TC is O(n) as it performs linear serach under the hood. SC is O(1) as no extra space is needed.
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")


# Linear Search
def linear_search(p_list, target):
    for i, value in enumerate(
        p_list
    ):  # TC is O(n) as it is a for loop and SC is O(1) as no extra space is required for this operation
        if value == target:
            return i
    return -1


print(linear_search(my_list, 60))
