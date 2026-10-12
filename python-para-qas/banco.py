


class contaBancaria:

    # construtor: é executado automaticamente quando criamos uma nova instância da classe
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f'Depósito de R$ {valor} realizado com sucesso! Novo saldo: R$ {self.saldo}')

    def consulta_saldo(self):
        print(f'O saldo atual é: {self.titular}: R$ {self.saldo}')


pablo = contaBancaria('Pablo', 1000)
stefany = contaBancaria('Stefany', 2000)


pablo.consulta_saldo()
pablo.depositar(500)
pablo.consulta_saldo()