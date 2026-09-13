str = "DanielAlex.com"
str1 = "Consulting firm"
str2 = "DanielAlex"
str3 = "great     "
str4 = "     great"

print(str[1])  # a
print(str[0:6])  # Daniel

print(str + str1)  # concatenation

print(str2 in str)  # True

splitted = str.split(".")  # split by .
print(splitted)
print(splitted[0])

stripped = str3.strip()  # remote white space
print(stripped)
leftStrip = str4.lstrip()
print(leftStrip)
