
#Aca estamos utilizando la palabra reservada del lenguaje para crear una clase y sus respectivos atributos y metodos. En este caso es la clase "Client"
class Client():
 
    def __init__(self, name, scnd_name, age, ID,):
        self.name = name
        self.scnd_name = scnd_name
        self.age = age
        self.ID = ID
        self.cart = []

    def __str__(self):
        return f'Mi nombre completo es {self.name} {self.scnd_name}, tengo {self.age} años y mi ID es {self.ID}'
    
    def add_to_cart(self, product):
       self.cart.append(product)
       return f'Añadiste un producto a tu carrito'
        
    def remove_from_cart(self, product):
        self.cart.remove(product)
        return f'Removiste un producto de tu carrito'

    def see_cart(self):
        return f'{self.cart}'



