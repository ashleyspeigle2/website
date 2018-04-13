def addDigits(num):
    #my solution
    if num == 0:
        return 0
    else:
        return (num % 10) + addDigits(num // 10)

print(addDigits)
