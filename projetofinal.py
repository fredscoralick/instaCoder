import numpy as np
import math
import csv

class Instagram():

    def __init__(self):
        self.dicionarioUsuarios = {}
    
    #Método para criar um dicionário onde a chave vai ser o vértice do grafo
    def adicionaVertice(self, vertice):
        self.dicionarioUsuarios[vertice] = {}

    #Método para fazer a leitura dos usuários a partir de um arquivo
    def lerUsuarios(self):
    #Abrir o arquivo com nome dos usuários
        with open('usuarios.csv', encoding='utf-8') as arquivoReferencia:
            tabelaUsuarios = csv.reader(arquivoReferencia, delimiter=',')
        
    #Para cada linha na tabela de usuários, pegar o segundo elemento e adicionar como vértice
            for linha in tabelaUsuarios:
                self.adicionaVertice(linha[1])      
        
    #Método para adicionar as conexões
    def conexoes(self, user1, user2, peso):
        self.dicionarioUsuarios[user1][user2] = peso

    #Método para ler as conexões a partir de um arquivo
    def lerConexoes(self):
        with open('conexoes.csv', encoding='utf-8') as arquivoAuxiliar:
            tabelaConexoes = csv.reader(arquivoAuxiliar, delimiter=',')

    #Para cada conexão na tabela de conexões, chame o método que adiciona as conexões
            for conexao in tabelaConexoes:
                self.conexoes(conexao[0], conexao[1], conexao[2])

    #Método para exibir quais são os usuários que o usuário passado pelo programador segue
    def exibeSeguidores(self, userName):
    #Lista vazia para adicionar o nome dos seguidores
        seguidores = []
        
    #Para cada linha no dicionário já criado, verificar a chave e pegar o primeiro valor (string com o nome do outro usuário)
        for linha in self.dicionarioUsuarios.items():
            for user in linha[1].items():
                if userName in user:
                    seguidores.append(linha[0])
        
        print(f'{userName} é seguido(a) por {len(seguidores)} pessoas. \n Essas pessoas são: {seguidores}\n')

    #Método para exibir quem o usuário passado pelo programador segue
    def exibeSeguindo(self, userName):
    #Contar a quantidade de chaves que são iguais ao nome do usuário
        seguidos = len(self.dicionarioUsuarios[userName].keys())
        print(f'{userName} segue {seguidos} pessoas. \n Essas pessoas são: {[*self.dicionarioUsuarios[userName].keys()]}\n')
    
    #Método para ordenar os stories de acordo com os melhores amigos e ordem alfabética
    def ordenaStories(self, userName):
        #Pegar os nomes das chaves correspondentes e transformar em lista através do *
        nomeAmigos = [*self.dicionarioUsuarios[userName].keys()]
        #Pegar os valores das chaves correspondentes e transformar em lista através do *
        valorAmigos = [*self.dicionarioUsuarios[userName].values()]
        melhoresAmigos = []
        amigosNormais = []
        listaOrdenada = []

        for idx, valor in enumerate(valorAmigos):
        #Se o valor for igual a 2, então essa conexão é um melhor amigo
            if valor == '2':
                melhoresAmigos.append(nomeAmigos[idx])
            else:
                amigosNormais.append(nomeAmigos[idx])
    
    
        print(f'Os melhores amigos de {userName} são: {melhoresAmigos}\n')
    #Ordenar as duas listas e mostrar a ordem dos stories
        listaOrdenada = sorted(melhoresAmigos) + sorted(amigosNormais)
        print(f'Os stories de {userName} aparecerão na seguinte ordem: {listaOrdenada}\n')

    #Método para encontrar quais são os top k influencers (top k mais seguidos)
    def encontraTopInfluencers(self, quantidade):
        contagemUsuarios = {}
        dicionarioMaiores = {}
    #Para cada linha no grafo maior
        for linha in self.dicionarioUsuarios.items():
    #Para cada usuário contido no segundo elemento da linha
            for user in linha[1].items():
    #Se o usuário na posição 0 não estiver no novo dicionário, adicioná-lo e colocar o valor 0
                if user[0] not in contagemUsuarios:
                    contagemUsuarios[user[0]] = 0 
        
        #Procurar no grafo maior os nomes dos usuários. a cada nome encontrado, somar 1 no valor do dicionário
        for item in self.dicionarioUsuarios:
            numeroSeguidores = 0
            for linha in self.dicionarioUsuarios.items():
                for user in linha[1].items():
                    if item in user:
                        numeroSeguidores += 1
            contagemUsuarios[item] = numeroSeguidores
        
        #Função sorted para ordenar os valores e colocar em um novo dicionário
        dicionarioMaiores = sorted(contagemUsuarios, key = contagemUsuarios.get, reverse=True)
            
    
        #print(contagemUsuarios)
        print(f"Os {quantidade} maiores influencers são : {dicionarioMaiores[:quantidade]}\n")
    
    #Método para encontrar o menor caminho entre os usuários (Busca em Largura)
    def encontraCaminho(self, origem, destino, visitados=None):
    #Criar uma fila, em que o seu primeiro elemento sempre será a origem
        fila = [origem]
    #Criar uma lista para armazenar todos nós os visitados
        visitados = []
    #Dicionário de predecessores, com a origem como chave e tendo peso nulo
        predecessor = {origem : None}
    
    #Enquanto a fila for maior que zero
        while len(fila) > 0:
    #Criar uma variável que é igual ao primeiro elemento da fila
            primeiroUsuario = fila[0]
    #Remover o primeiro elemento da fila
            fila = fila[1:]
    #Adicionar o primeiro elemento na lista de visitados
            visitados.append(primeiroUsuario)
    #Para cada chave no grafo, em que o nó é o primeiro elemento
            for adjacente in self.dicionarioUsuarios[primeiroUsuario].keys():
                #print(adjacente)
    #Se a chave for igual ao nó de destino
                if adjacente == destino:
                    pred = primeiroUsuario
                    caminhoContrario = [destino]
    #Enquanto a variável não for vazia
                    while pred is not None:
    #Adicionar a variável a lista do caminho contrário
                        caminhoContrario.append(pred)
                        pred = predecessor[pred]
                    
                    caminho = ''
    #Para cada elemento na lista de Caminho Contrário (invertida)
                    for no in caminhoContrario[::-1]:
                        caminho += f'{no} -> '
                    
                    return print(f'O menor caminho de conexão entre {origem} e {destino} é : {caminho[:-3]}\n')
    
    #Se a chabe não estiver na fila e não estiver na lista de visitados
                if adjacente not in fila and adjacente not in visitados:
    #Adicionar ao dicionário de predecessores o primeiro elemento
                    predecessor[adjacente] = primeiroUsuario
                    fila.append(adjacente)
        return False

meuInstagram = Instagram()
meuInstagram.lerUsuarios()
meuInstagram.lerConexoes()
meuInstagram.exibeSeguidores('helena42')
meuInstagram.exibeSeguindo('helena42')
meuInstagram.ordenaStories('helena42')
meuInstagram.encontraTopInfluencers(6)
meuInstagram.encontraCaminho('helena42', 'isadora45')
