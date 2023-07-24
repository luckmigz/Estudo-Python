class Filme: 
    def __init__(self, nome, ano,duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0
    
    def dar_like(self):
        self.likes += 1
    
    @property
    def likes(self):
         return self.__likes
     
    @property
    def nome(self):
        return self.__nome    
   
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
    
class Serie:
    def __init__(self,nome,ano,temp):
        self.nome = nome
        self.ano = ano
        self.temp = temp 

vingadores = Filme("vingadores - guerra infinita", 2018,160)
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}")

atlanta = Serie("Atlanta",2018,2)
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temp}")