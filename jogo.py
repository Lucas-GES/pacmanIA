import os
import time
from regras_jogo.personagens import Personagens
from regras_jogo.regras_pacman import construir_jogo
from agentes import construir_agente
from agentes.tipos import TiposAgentes

def ler_tempo(em_turnos=False):
    """ Se o jogo for em turnos, retorna a passada de 1 rodada.
    
    Se não for em turno, é continuo ou estratégico, retorna tempo
    preciso (ns) do relógio.
    """
    return 1 if em_turnos else time.time()

def iniciar_jogo():
    jogo = construir_jogo()
    personagem_jogador = jogo.registrarAgentePersonagem(Personagens.JOGADOR_PACMAN)
    
    tempo_de_jogo = 0
    print("Qual método de jogo você deseja utilizar? (Digite o número)")
    print("1) Agente humano")
    print("2) BFS")
    print("3) DFS")
    opcao = input()
    if opcao == '1':
        agente_jogador = construir_agente(TiposAgentes.PREPOSTO_HUMANO, Personagens.JOGADOR_PACMAN)
        while not jogo.game_over():
            os.system('cls||clear')
            jogo.print_labirinto()
                
            acao = agente_jogador.escolherProximaAcao()
            jogo.registrarProximaAcao(personagem_jogador, acao)
                
            jogo.atualizarEstado(1, 'humano')
            tempo_de_jogo += 1
        print('Jogo Finalizado')    
    elif opcao == '2':
        agente_jogador = construir_agente(TiposAgentes.AUTO_BFS, Personagens.JOGADOR_PACMAN)
        while not jogo.game_over():
            
            
            agente_jogador.get_bfs()
            
            movimentos = agente_jogador.get_movimentos()
            print(movimentos)
            for i in movimentos:
                os.system('cls||clear')
                jogo.print_labirinto()
                agente_jogador.set_movimento(i)
                
                acao = agente_jogador.escolherProximaAcao()
                jogo.registrarProximaAcao(personagem_jogador, acao)
                
                jogo.atualizarEstado(1, 'bfs')
                tempo_de_jogo += 1
                time.sleep(0.5)
    


if __name__ == '__main__':
    iniciar_jogo()