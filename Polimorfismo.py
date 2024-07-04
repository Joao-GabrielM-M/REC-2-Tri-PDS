# polimorfismo.py

# Classes Funcionario, Professor, Cozinheiro
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        pass


class Professor(Funcionario):
    def trabalhar(self):
        return f"{self.nome} está ensinando."


class Cozinheiro(Funcionario):
    def trabalhar(self):
        return f"{self.nome} está cozinhando."


# Classes Animal, Cachorro, Gato, Passaro, Porco
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass


class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome} está latindo."


class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} está miando."


class Passaro(Animal):
    def fazer_som(self):
        return f"{self.nome} está cantando."


class Porco(Animal):
    def fazer_som(self):
        return f"{self.nome} está grunhindo."


# Classes Veiculo, Caminhao, Carro, Moto
class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def mover(self):
        pass


class Caminhao(Veiculo):
    def mover(self):
        return f"O caminhão da marca {self.marca} está transportando carga."


class Carro(Veiculo):
    def mover(self):
        return f"O carro da marca {self.marca} está dirigindo na estrada."


class Moto(Veiculo):
    def mover(self):
        return f"A moto da marca {self.marca} está acelerando na pista."


# Código para testar os métodos polimórficos
if __name__ == "__main__":
    # Testando Funcionario, Professor e Cozinheiro
    prof = Professor("Carlos")
    coz = Cozinheiro("Maria")
    print(prof.trabalhar())
    print(coz.trabalhar())

    # Testando Animal, Cachorro, Gato, Passaro e Porco
    dog = Cachorro("Rex")
    cat = Gato("Mimi")
    bird = Passaro("Piupiu")
    pig = Porco("Babe")
    print(dog.fazer_som())
    print(cat.fazer_som())
    print(bird.fazer_som())
    print(pig.fazer_som())

    # Testando Veiculo, Caminhao, Carro e Moto
    truck = Caminhao("Volvo")
    car = Carro("Toyota")
    bike = Moto("Honda")
    print(truck.mover())
    print(car.mover())
    print(bike.mover())
