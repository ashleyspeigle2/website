## Ashley Speigle Lab 14 - Principles of Computing
## This program implements an alarm clock.
    ## It asks the user to enter a time and when that time occurs it will go off.

import time
import webbrowser
from time import strftime

def main():
    alarm = input("Please enter a time for an alarm (HH:MM AM/PM): ")

    while True:

        now = strftime("%I:%M %p")
        print(now)

        if alarm == now:
            
            print("Alarm")

            time.sleep(11)


            webbrowser.open("https://www.youtube.com/watch?v=iNpXCzaWW1s")

        else:
            print("no alarm")
            time.sleep(11)


main()
                  
## I was unable to get the local time to work so I found I could use strftime
## to work. From then the program was able to run.
