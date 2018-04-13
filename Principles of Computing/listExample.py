list1 = []

name = "Ashley"
x = 7
pi = 3.14

list1.append(name)
list1.append(x)
list1.append(pi)

list1 = ["Ashley", x, pi]
list2 = ["car", "cheese", 8]
list3 = [11, "lamp", "tree"]

list4 = [list1, list2, list3]

print(list4)

for list in list4:
    print(list)

x = 0
y = 2
print(list4[x][y])
