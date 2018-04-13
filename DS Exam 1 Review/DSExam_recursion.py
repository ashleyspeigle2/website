def addDigits(num):
    if len(num) == 0:
        return 0
    elif len(num) == 1:
        return num[0]
    else:
        leng = len(num)
        return num[0:leng // 2]+num[leng //2:]

addDigits(num)

print(addDigits(input("Enter a number:")))
    

