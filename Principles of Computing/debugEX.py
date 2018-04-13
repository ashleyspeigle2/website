print("Hello, World")
x=0

for i in range(50,2,-3):
    print(i)
    x=x+i
    print(x)
    for i in range(10):
        x=x+j
    print(x)

    if (x > 1000):
        print("The end.")
        exit()

