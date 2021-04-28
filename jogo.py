import os
from ambiente import Ambiente
from acoes import Acoes

class Jogo():

    def novoJogo():
        jogador = Ambiente.jogador

        for i in range(len(Ambiente.labirinto)):
            for j in range(len(Ambiente.labirinto[0])):
                if i == 8:
                    if  j == 4:
                        Ambiente.labirinto[i][j] = jogador

    def game_over():
        count = 0
        for i in range(len(Ambiente.labirinto)):
                for j in range(len(Ambiente.labirinto[0])):
                    if Ambiente.labirinto[i][j] == ".":
                        count += 1                   
        
        if count == 0:
            return True
        else:
            return False  


if __name__ == '__main__':

    Jogo.novoJogo()
    
    while Jogo.game_over() == False:
        os.system('cls||clear')
        Ambiente.ambiente(Ambiente.labirinto)
        print(Ambiente.get_posicao())
        Acoes.mover(input())
    
    os.system('cls||clear')
    Ambiente.ambiente(Ambiente.labirinto)