class Human:

    def __init__(self,name_input,country_input) -> None:
        self.name = name_input 
        self.country = country_input

    def greet(self):
        if self.country == 'France':
            return "Salut!"
        else:
            return "Hello"
        
h1 = Human("Raj" , "France")

print(h1.greet())