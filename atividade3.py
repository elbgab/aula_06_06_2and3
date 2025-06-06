class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def calcular_pagamento(self):
        return 0.0 


class Coordenador(Funcionario):
    def calcular_pagamento(self):
        return 8000.0  

class Desenvolvedor(Funcionario):
    def calcular_pagamento(self):
        return 6000.0  

class Estagiario(Funcionario):
    def calcular_pagamento(self):
        return 1500.0  


funcionarios = [
    Coordenador("Ana"),
    Desenvolvedor("Bruno"),
    Estagiario("Carlos"),
    Desenvolvedor("Diana"),
    Estagiario("Eduarda")
]

for funcionario in funcionarios:
    pagamento = funcionario.calcular_pagamento()
    print(f"{funcionario.nome} deve receber R$ {pagamento:.2f}")
