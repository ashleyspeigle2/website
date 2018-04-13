##Ashley Speigle
##Lab01: Data Structures
##This program determines the greates possible profit from a single purchase
##and sale of apples. Starting budget is $100.

def main():
    prices = [14, 6, 9, 7, 8, 10, 3, 9]
    profit = 0
    minimum = prices[0]
    for i in range(1, len(prices)):
        minimum = min(minimum, prices[i])
        profit = max(profit, prices[i] - minimum)

    print ("The greatest profit is",profit)

main()
