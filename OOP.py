class Calculator:
    num = 100  # class variables

    # default constructor
    def __init__(self, a, b):
        print("I am called automatically when object is created")
        self.firstNumber = a
        self.secondNumber = b

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num


obj = Calculator(2, 3)  # syntax to create objects in python
obj.getData()
print(obj.num)

obj1 = Calculator(4, 5)

print(obj1.Summation())
