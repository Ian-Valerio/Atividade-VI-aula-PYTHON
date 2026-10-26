class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    def mostrar_dados(self):
        print("Marca:", self.__marca)
        print("Modelo:", self.__modelo)
        print("Ano:", self.__ano)

    def acao(self):
        print("Veiculo cadastrado!")

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano


class Carro(Veiculo):
    def abrir_porta(self):
        print("O carro esta abrindo a porta!")

    def acao(self):
        print("O carro esta andando!")


class Moto(Veiculo):
    def empinar(self):
        print("A moto esta empinando!")

    def acao(self):
        print("A moto esta andando!")


carro = Carro("Toyota", "Corolla", 2024)
moto = Moto("Honda", "CB 300", 2023)

print("=== CARRO ===")
carro.mostrar_dados()
carro.abrir_porta()
carro.acao()

print("\n=== MOTO ===")
moto.mostrar_dados()
moto.empinar()
moto.acao()