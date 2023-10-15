import matplotlib.pyplot as plt
from random import randint

for i in range(20):
    list = []
    list.append(randint(1, 5))
    count1 = list.count(1) / len(list)
    count2 = list.count(2) / len(list)
    count3 = list.count(3) / len(list)
    count4 = list.count(4) / len(list)
    count5 = list.count(5) / len(list)

    counter1 = list.count(1)
    counter2 = list.count(2)
    counter3 = list.count(3)
    counter4 = list.count(4)
    counter5 = list.count(5)
# x axis is the number of occurrences
x_coords = [count1, count2, count3, count4, count5]

# y axis is the number of tries
y_coords = [counter1, counter2, counter3, counter4, counter5]

plt.bar(x_coords, y_coords, width=0.1, color=["blue", "green"])

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.title("Fuck me, why won't it import???")

plt.show()
