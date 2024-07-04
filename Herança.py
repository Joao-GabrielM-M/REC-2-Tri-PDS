# Heranca.py

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def relatorio(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")
        print(f"Departamento: {self.departamento}")


# Exemplo de uso das classes

# Criando objetos das classes
funcionario = Funcionario("Carlos", 3000)
gerente = Gerente("Ana", 8000, "Financeiro")

# Aumentando o salário de um funcionário
funcionario.aumentar_salario(10)  # Aumento de 10%
print(f"Novo salário do funcionário {funcionario.nome}: R$ {funcionario.salario:.2f}")

# Exibindo relatório de um gerente
gerente.relatorio()

# Aumentando o salário do gerente
gerente.aumentar_salario(15)  # Aumento de 15%
print(f"Novo salário do gerente {gerente.nome}: R$ {gerente.salario:.2f}")
gerente.relatorio()
