## Ashley Speigle
## This program prints out 2 numbers after being added, multiplied, and subtracted
## Lab02B1
def main():
	x = eval(input("Enter a number: "))
	y = eval(input("Enter another number: "))
	for i in range(1):
		z = x + y
		print("x + y =",z)
		z = x * y
		print("x * y =",z)
		z = x - y
		print("x - y =",z)

main()
