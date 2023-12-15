a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

d = a * 3
print(d)

e = len(a)
print(e)

f, g = max(a), min(b)
print(f, g)

i = sum(a)
print(i)


def cal_avg(list):
    avg = sum(list) / len(list)
    return avg


list = []
while True:
    inp = input("Enter a number: ")
    if inp == "D":
        print(cal_avg(list))
        break
    else:
        inp = float(inp)
    list.append(inp)
