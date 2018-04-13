num = input()

def factorial(n):
    try:
        n == 0

    except ValueError:
        print("You can only enter a number")

    else:
        return n * factorial(n - 1)


factorial(num)
