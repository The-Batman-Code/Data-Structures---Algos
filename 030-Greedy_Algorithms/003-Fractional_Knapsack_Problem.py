class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)  # O(nlogn)
    usedCapacity = 0
    totalValue = 0
    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value

        else:
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value

        if usedCapacity == capacity:
            break
    print(f"Total value obtained {totalValue}")
    # TC and SC of the above method is O(nlogn) and O(1) resp


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
cList = [item1, item2, item3]

knapsackMethod(cList, 50)
