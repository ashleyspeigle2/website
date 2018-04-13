def main():
    fileObject = open("hellotext.txt","w")
    print("Hello World", file=fileObject)
    fileObject.close()

main()
