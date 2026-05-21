class ContaBancaria:
    def __init__(self):
        #Inicia o saldo
        self.saldo = 1000

    def mostra_saldo(self):
        print(f"Você armazenou R${self.saldo:.2f}")

    def depositando(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Você depositou R${valor:.2f}")
        else:
            print("Você deve depositar um valor positivo")

    def saldo_final(self):
        print(f"Seu saldo atual é de R${self.saldo:.2f}")


valores = ContaBancaria()
valores.mostra_saldo()
valores.depositando(500)
valores.saldo_final()