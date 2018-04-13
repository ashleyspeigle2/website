def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit,"degrees farenheit.")

    if fahrenheit > 90:
        print("It is extremely hot, dress accordingly.")

    if fahrenheit < 30:
        print("It is really cold, dress warmly.")

main()
