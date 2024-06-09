class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot]
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

    # TC and SC of the above method is O(1) and SC id O(n) as we are using recursion stack


vertices = ["A", "B", "C", "D", "E"]
ds = DisjointSet(vertices)

ds = DisjointSet(vertices)
ds.union("A", "B")
ds.union("A", "C")
print(ds.find("A"))
