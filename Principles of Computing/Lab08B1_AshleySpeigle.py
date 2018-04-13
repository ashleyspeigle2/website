#Ashley Speigle
    #This program uses the str.format() function and sub-indexing function
        #to create sentences
def main():
    # This part uses subindexing
    
    p1 = ["baseball", 2, "Jorge Polanco"]
    p2 = ["football", 12, "Harrison Butker"]
    p3 = ["League of Legends", 1880,"Nightblue3"]

    print(p1[2],"scored",p1[1],"points in this weekend's",p1[0],"match")

    print(p2[2],"scored",p2[1],"points in this weekend's",p2[0],"match")

    print(p3[2],"scored",p3[1],"points in this weekend's",p3[0],"match")

    # This part uses str.format()

    baseball_string = "{} scored {} points in this weekend's {} match."
    print(baseball_string.format("Jorge Polanco", 2, "baseball"))

    football_string = "{} scored {} points in this weekend's {} match."
    print(football_string.format("Harrison Butker", 12, "football"))

    LoL_string = "{} scored {} points in this weekend's {} match."
    print(LoL_string.format("Nightblue3", 1880, "League of Legends"))

main() 

# I did not know which way was correct so I went ahead and did both. 
