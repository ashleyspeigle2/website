def main():
    fileObject = open("exampleout.txt", "w")
    print("This is a sample text", file = fileObject)
    fileObject.close()
main()
