numdays = int(input("How many days' temperatures? "))
total = 0
temp = []
for i in range(0, numdays):
    nextday = int(input("Day " + str(i + 1) + "'s high temperature: "))
    temp.append(nextday)

avg = round(sum(temp) / numdays, 2)
print("Average temperature: " + str(avg))

above_avg_list = [item if item > avg else 0 for item in temp]
above_avg_days = len(above_avg_list) - above_avg_list.count(0)
print("Days above average: " + str(above_avg_days))
