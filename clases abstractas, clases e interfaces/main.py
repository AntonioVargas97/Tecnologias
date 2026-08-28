from abc import(ABC, abstractmethod)


class Personaje(ABC):

    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def recibir_danio(self, cantidad):
        self.vida -= cantidad
        print("recibe {cantidad} de danio")
        print("vida restante: ", {self.vida})

    @abstractmethod
    def atacar(self, objetivo):
        pass


class Icurable(ABC):

    @abstractmethod
    def curar(self, objetivo):
        pass

class Guerrero(Personaje):

    def atacar(self):
        print(f"{self.nombre} ataca con su espada")

class Mago(Personaje):

    def atacar(self):
        print(f"{self.nombre} ataca con bola de fuego")

    def curar(self, objetivo):
        objetivo.vida += 20
        print(f"{self.nombre} cura a {objetivo.nombre} y le devuelve 20 de vida")

class Soporte(Personaje):

    def atacar(self):
        print(f"{self.nombre} ataca con baston")

    def curar(self, objetivo):
        objetivo.vida += 20
        print(f"{self.nombre} cura a {objetivo.nombre} y le devuelve 20 de vida")



