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
    agente_jogador = construir_agente(TiposAgentes.PREPOSTO_HUMANO, Personagens.JOGADOR_PACMAN)
    
    tempo_de_jogo = 0
    while not jogo.game_over():
        os.system('cls||clear')
        jogo.print_labirinto()
        
        acao = agente_jogador.escolherProximaAcao()
        jogo.registrarProximaAcao(personagem_jogador, acao)
        
        jogo.atualizarEstado(1)
        tempo_de_jogo += 1
    
    # while game_over() == False:
    #     os.system('cls||clear')
    #     Ambiente.ambiente(Ambiente.labirinto)
    #     print(Ambiente.get_posicao())
    #     Acoes.mover(input())

    # os.system('cls||clear')
    # Ambiente.ambiente(Ambiente.labirinto)


if __name__ == '__main__':
    iniciar_jogo()