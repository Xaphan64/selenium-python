greeting = "Good Morning"

if greeting == "Morning":
    print("condition matches")
else:
    print("condition doesn't match")
print("if/else condition code is completed")

# for loop
obj = [2, 3, 5, 7, 9]

for i in obj:
    print(i * 2)

# sum of First Natural numbers 1+2+3+4=5 = 15
sum = 0

for j in range(1, 6):  # print all numbers from 1 to 5
    sum += j

print(f"sum: {sum}")

print("*************************")
for k in range(1, 10, 2):
    print(k)

print("*************************")
for m in range(10):  # start automatically from 0 if no starting value is defined
    print(m)
