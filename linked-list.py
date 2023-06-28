class Node:
    
    def __init__(self , value):
        self.data = value
        self.next_address = None


class LinkedList:

    # create empty LinkedList

    def __init__(self):
        self.header = None
        self.n = 0                                # no.of nodes in LL 

    
    #  len()

    def __len__(self):
        return self.n


    #  insert from head 

    def insert_head(self , value):

        new_node = Node(value)

        new_node.next_address = self.header

        self.header = new_node

        self.n = self.n + 1



    #  Traverse , Print 


    def __str__(self):

        current_location = self.header
        result = ''

        while current_location != None:
            
            result = result + str(current_location.data) + '->'
            
            current_location = current_location.next_address
    
        return result[:-2]


    # Insert from Tail 


    def append(self,value):

        new_node = Node(value)

        if self.header == None:
            self.header = new_node
            self.n = self.n + 1 
            return

        current = self.header

        while current.next_address != None:
    
            current = current.next_address
            
        current.next_address = new_node
        self.n = self.n + 1


    #  Insert_after()

    def insert_after(self , after_var_insert , value):
        new_node = Node(value)

        current = self.header
        
        while current != None:
            if current.data == after_var_insert:
                break
            current = current.next_address
            
        if current != None:
            new_node.next_address = current.next_address
            current.next_address = new_node
        else:
            return 'Item not found'

        
    # clear()

    def clear(self):
        self.header = None
        self.n = 0


    # delete the head node 

    def delete_head(self):
        self.header = self.header.next_address
        self.n = self.n - 1

    #  delete tail or pop()

    def pop(self):
        
        current = self.header

        while current.next_address.next_address != None:
            current = current.next_address

        current.next_address = None
        self.n = self.n - 1


    # remove a value from middle 

    def remove(self,remove_value):

        current = self.header

        while current.next_address != None:

            if current.next_address.data == remove_value:
                break
            current = current.next_address

        if current.next_address != None:
            current.next_address = current.next_address.next_address

        else:
            return 'Not found'


    #  search()



    def search(self , value):
        
        current = self.header
        position = 0

        while current != None:
            if current.data == value:
                return position

            position = position + 1
            current = current.next_address
        return 'Not found'


    #  get item based on index 

    def __get_item__(self , index ):

        current = self.header
        position = 0

        while current != None:
            if position == index:
                return current.data
                
            position = position + 1
            current = current.next_address



if __name__ == '__main__':
    l = LinkedList()
    l.insert_head(1)
    l.insert_head(2)
    l.insert_head(3)

    l.append(7)
    print(l.search(7))
    