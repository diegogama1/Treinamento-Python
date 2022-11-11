### vamos criar uma conta###

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        ## usamos esta funcao para construir um objeto
        print("contruindo objeto ...{}".format(self))
        #self é a referencia que sabe encontrar o memso objeto que esta
        #na memoria
        self.__numero = numero ## defini os atributos(da clase),da conta...
        self.__titular = titular ## __ unsando este comando mostra que
        ## o atributo é privado
        self.__saldo = saldo
        self.__limite = limite

##from conta import Conta
##conta = Conta(123, "Nico", 55.0, 1000.0)
##uso este comando para puxar a conta do console, e criando os
## posso buscar outras contas, ex: conta2 = Conta(321, "Joao", 100.0, 1000.0).

    def extrato(self):
        print("saldo de {} do titular {}". format(self.__saldo, self.__titular))
## com esta funcao consigo ter acesso a mais de uma conta. n contas.

    def deposita(self, valor):
        self.__saldo += valor
        #conta.deposita(20.0)
        # chamo o conta.extrato(),

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
#com o metodo acima, definos valor que pode ser sacado da conta

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        #no saca, é o mesmo de deposita.
        else:
            print("o valor {} passou o limite". format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
    #def get_limite(self):
        return self.__limite
    ##get é usado para buscar uma informacao na conta###
    ##set é usado para alterar algo, mas nao nos retorna alguma valor##
    @limite.setter
    def limite(self, limite): #usando o @limite.setter nao preciso usar o set.
        self.__limite = limite
    @staticmethod
    def codigo_banco():
        return "001"