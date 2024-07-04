class Validacao:
    def __init__(self, nome, idade, sexo, numero_chamada, serie, ano_colegio, cidade, estado, pais):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.numero_chamada = numero_chamada
        self.serie = serie
        self.ano_colegio = ano_colegio
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    @staticmethod
    def e_numero_positivo(numero):
        return numero > 0

    @staticmethod
    def verifica_positivo_negativo_zero(numero):
        if numero > 0:
            return "positivo"
        elif numero < 0:
            return "negativo"
        else:
            return "zero"

    @staticmethod
    def valida_par_impar(numero):
        return "par" if numero % 2 == 0 else "ímpar"

    @staticmethod
    def e_numero_primo(numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    @staticmethod
    def valida_idade(idade):
        return 0 <= idade <= 100

    @staticmethod
    def classifica_idade(idade, nome):
        if idade < 2:
            return f"{nome} é um bebê"
        elif idade < 12:
            return f"{nome} é uma criança"
        elif idade < 18:
            return f"{nome} é um adolescente"
        elif idade < 60:
            return f"{nome} é um adulto"
        else:
            return f"{nome} é um idoso"

    @staticmethod
    def valida_string_minimo_5_caracteres(string):
        return len(string) >= 5

    @staticmethod
    def quantidade_caracteres_string(string):
        return len(string)

    @staticmethod
    def quantidade_elementos_array(array):
        return len(array)

    @staticmethod
    def verifica_numero_intervalo(numero, inicio, fim):
        return inicio <= numero <= fim


# Exemplo de uso das funções

validador = Validacao("João", 25, "M", 123, "5ª série", 2024, "São Paulo", "SP", "Brasil")

print(validador.e_numero_positivo(10))  # True
print(validador.verifica_positivo_negativo_zero(-5))  # "negativo"
print(validador.valida_par_impar(4))  # "par"
print(validador.e_numero_primo(7))  # True
print(validador.valida_idade(50))  # True
print(validador.classifica_idade(3, "Ana"))  # "Ana é uma criança"
print(validador.valida_string_minimo_5_caracteres("Python"))  # True
print(validador.quantidade_caracteres_string("Python"))  # 6
print(validador.quantidade_elementos_array([1, 2, 3, 4, 5]))  # 5
print(validador.verifica_numero_intervalo(15, 10, 20))  # True
