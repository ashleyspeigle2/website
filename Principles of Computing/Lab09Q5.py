f = open("poem.txt","r")
l = f.readlines()
cur = 0
for i in l:
    print(cur, i)
    cur += 1
