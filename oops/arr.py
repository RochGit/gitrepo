class MyArray:

    def __init__(self) -> None:
        self.total_size = 1
        self.items_in_arr = 0
        self.arr = []

    def __len__(self):
        return self.items_in_arr
    
    def __str__(self) -> str:
        return self.arr


    def add_item_in_array(self,item_to_be_added):
        self.arr.append(item_to_be_added)

        # if self.items_in_arr == self.total_size:
            
            
        

l = MyArray()

print(len(l))

l.add_item_in_array(2)

print(len(l))

print(l)
