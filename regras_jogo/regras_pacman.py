from .personagens import Personagens
from .regras_abstratas import AbstractRegrasJogo
from acoes import AcoesJogador, DirecaoMoverPacman

class RegrasPacman():
    def __init__(self) -> None:
        super().__init__()
        labirinto_completo = [
            ["█","█","█","█","█","█","█","█","█","█","█","█"],
            ["█"," "," "," "," "," "," "," "," "," "," ","█"],
            ["█"," "," ",".","█","█","█"," "," ","█"," ","█"],
            ["█"," ","█","."," "," "," "," ","█","█"," ","█"],
            ["█"," "," ","."," "," "," "," "," "," "," ","█"],
            ["█"," ","█",".","█"," ","█"," ","█"," "," ","█"],
            ["█"," ","█",".","█","█","█"," ","█"," "," ","█"],
            ["█"," "," ",".",".","█"," "," "," "," "," ","█"],
            ["█"," "," ","█","."," "," ","█"," ","█"," ","█"],
            ["█","█","█","█","█","█","█","█","█","█","█","█"],
        ]
        self.labirinto = labirinto_completo
        self.id_personagens = {Personagens.JOGADOR_PACMAN: 0}
        self.acoes_personagens = {0: None}
        self.msg_jogador = None
        self.jogador = 'c'
        self.inserirJogador()
        
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
        
    def atualizarEstado(self, diferencial_tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        acao_jogador = self.acoes_personagens[self.id_personagens[Personagens.JOGADOR_PACMAN]]
        if acao_jogador.tipo == AcoesJogador.MOVER_PACMAN:
            if acao_jogador.parametros == DirecaoMoverPacman.ESQUERDA:
                for i in range(len(self.labirinto)):
                    for j in range(len(self.labirinto[0])):
                        if self.labirinto[i][j] == self.jogador:
                            y = j-1
                            if self.valida_movimento(i, y):
                                self.labirinto[i][y] = self.jogador
                                self.labirinto[i][j] = " "

            elif acao_jogador.parametros == DirecaoMoverPacman.DIREITA:
                for i in range(len(self.labirinto)):
                    for j in range(len(self.labirinto[0])):
                        if self.labirinto[i][j] == self.jogador:
                            y = j+1
                            if self.valida_movimento(i, y):
                                self.labirinto[i][y] = self.jogador
                                self.labirinto[i][j] = " "
                                break
            
            elif acao_jogador.parametros == DirecaoMoverPacman.CIMA:
                for i in range(len(self.labirinto)):
                    for j in range(len(self.labirinto[0])):
                        if self.labirinto[i][j] == self.jogador:
                            x = i-1
                            if self.valida_movimento(x, j):
                                self.labirinto[x][j] = self.jogador
                                self.labirinto[i][j] = " "
                                break

            elif acao_jogador.parametros == DirecaoMoverPacman.BAIXO:
                for i in reversed(range(len(self.labirinto))):
                    for j in range(len(self.labirinto[0])):
                        if self.labirinto[i][j] == self.jogador:
                            x = i+1
                            if self.valida_movimento(x, j):
                                self.labirinto[x][j] = self.jogador
                                self.labirinto[i][j] = " "
                                break
        
    def inserirJogador(self) -> None:
        for i in range(len(self.labirinto)):
            for j in range(len(self.labirinto[0])):
                if i == 8:
                    if j == 5:
                        self.labirinto[i][j] = self.jogador
    
    def get_jogador(self):
        for i in range(len(self.labirinto)):
            for j in range(len(self.labirinto[0])):
                if self.labirinto[i][j] == 'c':
                    x = i
                    y = j
                    return x, y
    
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
    