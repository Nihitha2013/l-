class Emp:
    def ___init__(self):
        print("Employee class")
    def __del__(self):
        print("Destructor")

    def objfun():
        print("Object created")
        o=Emp()
        print("Object function end")
        return o
print("Calling function")
obj=Emp.objfun()

print("Program End")