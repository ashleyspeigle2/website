def main():
    text = "the brown fox"
    textlist = text.split()
    if len(textlist) == 2:
        if len(text) == 13:
            print(1)
        else:
            print(2)
    else:
        if textlist[2] == "brown":
            print(3)
        elif textlist[1] == "brown":
            print(4)
        else:
            print(5)

main()
