class Parent:

    def __init__(self,num) -> None:
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):

    def __init__(self, num,val) -> None:
        super().__init__(num)
        self.__val = val 

    def get_val(self):
        return self.__val
    
c = Child(100,200)

print(c.get_num())
print(c.get_val())