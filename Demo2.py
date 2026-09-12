# array (lists)
values = [1, 2, "daniel", 4, 5]

print(values[0])  # 1
print(values[3])  # 4
print(values[-1])  # get the last item in the array
print(values[1:3])  # 2, daniel and 4
values.insert(3, "alex")  # add alex at index
print(values)
values.append("end")  # adds end at the end of the array
print(values)

values[2] = "TEST"  # to update a value
print(values)

del values[0]  # delete the value
print(values)

# tuple is immutable
val = (1, 2, "daniel", 4.5)
# val[2] = "test"
print(val)

# dictionary
dictionary = {"a": 2, 4: "bcd", "c": "Hello world"}

print(dictionary[4])
print(dictionary["c"])

dict = {}
dict["firstname"] = "Daniel"
dict["lastname"] = "Alex"
dict["gender"] = "Male"
print(dict)
