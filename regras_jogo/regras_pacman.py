from .personagens import Personagens
from .regras_abstratas import AbstractRegrasJogo
from acoes import AcoesJogador, DirecaoMoverPacman

class RegrasPacman():
    def __init__(self) -> None:
        super().__init__()
        labirinto_completo = [
            ["█","█","█","█","█","█","█","█","█","█","█","█"],
            ["█"," "," "," "," "," "," "," "," "," ",".","█"],
            ["█"," ","█"," ","█","█","█"," ","█","█"," ","█"],
            ["█"," ","█"," ","█","█","█"," ","█","█"," ","█"],
            ["█"," "," "," "," "," "," "," "," "," "," ","█"],
            ["█"," ","█"," ","█","█","█"," ","█"," ","█","█"],
            ["█"," ","█"," ","█","█","█"," ","█"," ","█","█"],
            ["█"," ","█"," ","█","█","█"," ","█"," ","█","█"],
            ["█"," "," "," "," ","C"," "," "," "," ","█","█"],
            ["█","█","█","█","█","█","█","█","█","█","█","█"],
        ]
        self.labirinto = labirinto_completo
        self.id_personagens = {Personagens.JOGADOR_PACMAN: 0}
        self.acoes_personagens = {0: None}
        self.msg_jogador = None
        self.caminho = []
        self.inicial = []
        
    def valida_movimento(self, x, y):
        if(self.labirinto[x][y] == '█'):
            return False
        else:
            return True
        
    def registrarProximaAcao(self, id_agente, acao) -> None:
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        self.acoes_personagens[id_agente] = acao
        
    def atualizarEstado(self, diferencial_tempo, tipo_jogador):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        acao_jogador = self.acoes_personagens[self.id_personagens[Personagens.JOGADOR_PACMAN]]
        if acao_jogador.tipo == AcoesJogador.MOVER_PACMAN:
            if acao_jogador.parametros == DirecaoMoverPacman.ESQUERDA:
                for i in range(len(self.labirinto)):
                    for j in range(len(self.labirinto[0])):
                        if self.labirinto[i][j] == "C":
                            y = j-1
                            if self.valida_movimento(i, y):
                                if tipo_jogador == 'humano':
                                    self.labirinto[i][y] = "C"
                                    self.labirinto[i][j] = " "
                                elif tipo_jogador == 'bfs':
                                    existe = False
                                    if self.existe_caminho([i,y]):
                                        existe = True
                                    self.labirinto[i][y] = "C"
                                    self.marca_caminho([i, y])
                                    if self.existe_caminho([i,j]) and existe:
                                        self.labirinto[i][j] = " "
                                        self.deleta_caminho([i, j])
                                    else:
                                        self.labirinto[i][j] = "*"
                                    
                                    

            elif acao_jogador.parametros == DirecaoMoverPacman.DIREITA:
                for i in range(len(self.labirinto)):
                    for j in range(len(self.labirinto[0])):
                        if self.labirinto[i][j] == "C":
                            y = j+1
                            if self.valida_movimento(i, y):
                                if tipo_jogador == 'humano':
                                    self.labirinto[i][y] = "C"
                                    self.labirinto[i][j] = " "
                                    break
                                elif tipo_jogador == 'bfs':
                                    existe = False
                                    if self.existe_caminho([i,y]):
                                        existe = True
                                    self.labirinto[i][y] = "C"
                                    self.marca_caminho([i, y])
                                    if self.existe_caminho([i,j]) and existe:
                                        self.labirinto[i][j] = " "
                                        self.deleta_caminho([i, j])
                                    else:
                                        self.labirinto[i][j] = "*"
                                    break
            
            elif acao_jogador.parametros == DirecaoMoverPacman.CIMA:
                for i in range(len(self.labirinto)):
                    for j in range(len(self.labirinto[0])):
                        if self.labirinto[i][j] == "C":
                            x = i-1
                            if self.valida_movimento(x, j):
                                if tipo_jogador == 'humano':
                                    self.labirinto[x][j] = "C"
                                    self.labirinto[i][j] = " "
                                    break
                                elif tipo_jogador == 'bfs':
                                    existe = False
                                    if self.existe_caminho([x,j]):
                                        existe = True
                                    self.labirinto[x][j] = "C"
                                    self.marca_caminho([x,j])
                                    if self.existe_caminho([i,j]) and existe:
                                        self.labirinto[i][j] = " "
                                        self.deleta_caminho([i, j])
                                    else:
                                        self.labirinto[i][j] = "*"
                                    break

            elif acao_jogador.parametros == DirecaoMoverPacman.BAIXO:
                for i in reversed(range(len(self.labirinto))):
                    for j in range(len(self.labirinto[0])):
                        if self.labirinto[i][j] == "C":
                            x = i+1
                            if self.valida_movimento(x, j):
                                if tipo_jogador == 'humano':
                                    self.labirinto[x][j] = "C"
                                    self.labirinto[i][j] = " "
                                    break
                                elif tipo_jogador == 'bfs':
                                    existe = False
                                    if self.existe_caminho([x,j]):
                                        existe = True
                                    self.labirinto[x][j] = "C"
                                    self.marca_caminho([x,j])
                                    if self.existe_caminho([i,j]) and existe:
                                        self.labirinto[i][j] = " "
                                        self.deleta_caminho([i, j])
                                    else:
                                        self.labirinto[i][j] = "*"
                                    break
    def inserirJogador(self) -> None:
        for i in range(len(self.labirinto)):
            for j in range(len(self.labirinto[0])):
                if i == 8:
                    if j == 5:
                        self.labirinto[i][j] = "C"
                        self.inicial = i, j
    
    def get_jogador(self):
        for i in range(len(self.labirinto)):
            for j in range(len(self.labirinto[0])):
                if self.labirinto[i][j] == 'C':
                    x = i
                    y = j
                    return x, y
    
    def marca_caminho(self, localizacao) -> None:
        self.caminho.append(localizacao)
        
    
    def deleta_caminho(self, localizacao) -> None:
        for i in self.caminho:
            if i == localizacao:
                self.caminho.remove(i)
                
    def existe_caminho(self, localizacao) -> bool:
        for i in range(len(self.caminho)):
            if self.caminho[i] == localizacao:
                return True
        return False
            
    
    @staticmethod
    def proxima_acao(self, movimento):
        pass
    
    def registrarAgentePersonagem(self, personagem):
        """ Cria ou recupera id de um personagem agente.
        """
        return self.id_personagens[personagem]
    
    def game_over(self):
        count = 0
        for i in range(len(self.labirinto)):
            for j in range(len(self.labirinto[0])):
                if self.labirinto[i][j] == ".":
                    count += 1

        if count == 0:
            return True
        else:
            return False
        
    def get_labirinto(self):
        return self.labirinto
    
    def print_labirinto(self):
        for i in range(len(self.labirinto)):                
            for j in range(len(self.labirinto[0])):                
                if j == 11:
                    print(self.labirinto[i][j])
                else:
                    print(str(self.labirinto[i][j]) + "", end="")
        
def construir_jogo(*args,**kwargs):
    return RegrasPacman()
    