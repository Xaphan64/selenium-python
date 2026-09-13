# ItemsInCart = 0

# # raise manual error
# if ItemsInCart != 2:
#     raise Exception("Products Cart count not matching")

# # specific error
# assert ItemsInCart == 2

# try/except
try:
    with open("filelog.txt", "r") as reader:
        print("try block worked")
        reader.read()
# custom message
except:
    print("somehow i reached this block because try fails")


try:
    with open("filelog.txt", "r") as reader:
        print("try block worked")
        reader.read()
# python specific descriptive error
except Exception as e:
    print(e)
finally:
    print("cleanin up resources")
