import ctypes

class MeraList:

    def __init__(self):
        self.size = 1
        self.n = 0

        # create c-type array with size = self.size 
        self.A = self.__make_array(self.size)

    def __make_array(self,size):
        return (size*ctypes.py_object)() # creates a c type array with size (static , referntial )


#  creating our own len() func


    def __len__(self):
        return self.n


#  append()


    def append(self,item):
        
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)

        self.A[self.n] = item
        self.n = self.n + 1


    def __resize(self ,new_size ):
        # create a new array with size double ( we are choosing to keep it double , can be further optimized )
        
        B = self.__make_array(new_size)
        self.size = new_size

        # copy content from A to new array B 

        for i in range(self.n):
            B[i] = self.A[i]
        
        # ressaign A as our logic is done with A

        self.A = B 


        #  print()

    def __str__(self):

        result = ''

        for i in range(self.n):
            result = result + str(self.A[i]) + ',' 
        return '[' + result[:-1] + ']'

#  index function ->  arr[i]


    # def __getattribute__(self, index):
    #     if 0 <= index < self.n:
    #         return self.A[index]
    #     return 'IndexError'

#   pop()

    def pop(self):
        if self.n == 0:
            return '[]'
        print( self.A[self.n-1] )
        self.n = self.n-1


#  clear()


    def clear(self):
        self.size = 1
        self.n = 0

#  the index()  || video followed approach find()

    def find(self , item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError'


#  insert()

    def insert(self , position , item):
        
        if self.n == self.size:
            self.__resize(self.n*2)
        
        for i in range( self.n , position , -1 ):
            self.A[i] = self.A[i-1]

        self.A[position] = item
        self.n = self.n+1


# del()





if __name__ == '__main__':
    L = MeraList()

    L.append(1)
    L.append(1)
    L.append(1)
    L.append(1)
    L.append(4)

