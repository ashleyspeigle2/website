##Ashley Speigle
##This program will print out hello world after 10 seconds using a timer

from threading import Timer

def hello():
    print ("hello, world")

    t = Timer(10.0, hello)
    t.start()

hello()
