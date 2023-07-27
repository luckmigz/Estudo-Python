class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        
    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'
    
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    


class Filme(Programa): 
    def __init__(self, nome, ano,duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self._likes} likes'

 

   
class Serie(Programa):
    def __init__(self,nome,ano,temp):
        super().__init__(nome, ano)
        self.temporadas = temp
        
    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'



vingadores = Filme("vingadores - guerra infinita", 2018,160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta = Serie("Atlanta",2018,2)
atlanta.dar_likes()
atlanta.dar_likes()

lista = [vingadores, atlanta]

for programa in lista:
    print(programa)
    
    
