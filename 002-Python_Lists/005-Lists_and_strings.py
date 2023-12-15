a = "spam"
b = list(a)
print(b)

c = "spam spam spam"
d = c.split()
print(d)

e = "spam-spam-spam"
f = e.split("-")
print(f)

print("-".join(f))
