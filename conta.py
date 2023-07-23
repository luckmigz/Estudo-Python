class Conta:
    def __init__(self,numero,titular,saldo,limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
        print("Const {}".format(self))
        
    # Objetos de ação/ Funções	
    
    def deposita(self,valor):
        self.__saldo =+ valor
        
    def saca(self,valor): 
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))
            
    def __pode_sacar(self, valor_a_sacar): 
        valor_disp = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disp
      
    def extrato(self):
        print("Saldo de {} R$ do titular {}".format(self.__saldo,self.__titular))
        
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)   
        
    # Objetos de propriedade 
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self,limite):
        self.__limite = limite
        
    @property
    def titular(self):
        return self.__titular
    
    @property
    def codigo_banco(self):
        return self.__codigo_banco
    
    # Metodos estaticos 
    
    @staticmethod
    def codigos_banco():
        return {"BB":"001", "Caixa": "104", "Bradesco": "273"}