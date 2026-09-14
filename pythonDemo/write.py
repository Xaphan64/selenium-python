with open("test.txt", "r") as reader:
    # read the file and store all the line in list
    content = reader.readlines()
    # reverse the list
    reversedList = reversed(content)
    # write the list back to the file
    with open("test.txt", "w") as writer:
        for line in reversedList:
            writer.write(line)
