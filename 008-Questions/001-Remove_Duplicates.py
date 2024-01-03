class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        # Head of list
        self.head = None

    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.value)
            temp = temp.next
            if temp is None:
                break
            result += str(" -> ")
        return result

    def duplicates(self):
        track = {}
        temp = self.head
        while temp:
            if temp.value not in track.keys():
                track.update({temp.value: 1})
            else:
                track[temp.value] += 1
            temp = temp.next
        print(track)
        list = []
        for key, value in track.items():
            if value > 1:
                list.append(key)
        for i in track.keys():
            while self.head.value in list:
                self.head = self.head.next
                if self.head is None:
                    return None
            if track[i] > 1:
                temp2 = self.head
                while temp2.next:
                    if temp2.next.value == i:
                        temp2.next = temp2.next.next
                        temp2 = self.head
                    else:
                        temp2 = temp2.next
                    print(self)
            else:
                continue
        return self.head


list = LinkedList()
list.head = Node(2)
list.head.next = Node(2)
list.head.next.next = Node(2)
list.head.next.next.next = Node(2)
list.head.next.next.next.next = Node(3)
list.head.next.next.next.next.next = Node(2)
list.head.next.next.next.next.next.next = Node(5)
print(list)
print(list.duplicates())
print(list)
