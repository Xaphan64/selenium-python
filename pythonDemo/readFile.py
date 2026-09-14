file = open("test.txt")
# read all the content of the file
print(file.read())
print("***********************")
file.close()

file2 = open("test.txt")
# read only the first 9 characters of the file
print(file2.read(9))
print("***********************")
file2.close()

file3 = open("test.txt")
# read only 1st line
print(file3.readline())
print("***********************")
file3.close()

# print line by line using readline method
file4 = open("test.txt")
line = file4.readline()
while line != "":
    print(line)
    # print the next line
    line = file4.readline()
    print("*****line separataor*****")

#  same as above but with for loop
file5 = open("test.txt")
for line in file5.readlines():
    print(line)
