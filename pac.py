from ambiente import Ambiente
from actions import Actions
from agenteBFS import AgenteBFS
from agenteASTAR import Node
import os

class Pac():
    def iniciar_jogo():        
    
        Ambiente.get_labirinto()
        Ambiente.inserirJogador()
        
        print("1 - Humano")
        print("2 - BFS")
        print("3 - A*")
        case = int(input())

        if case == 1:        
            tempo_de_jogo = 0
            while not Ambiente.game_over():
                os.system('cls||clear')
                Ambiente.print_labirinto()
                
                acao = input()
                Actions.atualizarEstado(acao)        
                
                Ambiente.get_labirinto()
                tempo_de_jogo += 1
                
            print(tempo_de_jogo)
        if case == 2:
            AgenteBFS.exec()
        
        if case == 3:
            Node.main()

        Ambiente.get_labirinto()


if __name__ == '__main__':
    Pac.iniciar_jogo()