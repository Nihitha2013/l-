class f1:
    def __init__(self):
        self.str1=""
    def enter(self):
        self.str1=input("Enter the string:")
    def printfun(self):
        print("Result is:", self.str1.upper())

s1=f1()
s1.enter()
s1.printfun()