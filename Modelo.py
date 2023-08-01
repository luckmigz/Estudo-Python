

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
    
class Playlist():
    def __init__(self,nome,programas):
        self.nome = nome
        self.__programas = programas
        
    def __getitem__(self,item):
        return self.__programas[item]
    
    def __len__(self):
        return len(self.__programas)
    
    @property
    def listagem(self):
        return self.__programas
    
    @property
    def tamanho(self):
        return( self.__programas)

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


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

lista = [atlanta, vingadores, demolidor, tmep]
playlist = Playlist('fim de semana', lista)

for programa in lista:
    print(programa)

print(f'Tamanho: {len(playlist.listagem)}')
