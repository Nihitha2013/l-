class rect:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.length*self.width
    

obj=rect(9,8)
result=obj.calculate_area()
print("Area of rectangle:",result)