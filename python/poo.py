class Persona():
    # Definiendo atributos (cualidades)
    def __init__(self,nombre,apellido,id):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id

    # Un metodo (funcionalidad)
    def info(self):
        print(f"Soy {self.nombre} {self.apellido}")

class Dispositivo:
    def __init__(self,marca,precio):
        self.marca = marca
        self.precio = precio
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"{self.marca} encendido")

    def apagar(self):
        self.encender = False
        print(f"{self.marca} apagado")

    def info(self):
        return f"{self.marca} - {self.precio}"


class Celular(Dispositivo):
    def __init__(self,marca,precio,capacidad):
        super().__init__(marca,precio)
        self.capacidad = capacidad

    def llamar(self,numero):
        self.numero = numero
        print(f"Llamando al numero {self.numero}")
    
    def info(self):
        return f"{super().info()} - {self.capacidad}GB" 
persona1 = Persona("Fredy","Soto",123456)

# Abstracción
persona1.apellido

persona1.info()


celular1 = Celular("iphone 17 Pro Max","1500","256")

celular1.marca
celular1.encender()
celular1.apagar()

celular1.llamar("3043273170")
print(celular1.info())
