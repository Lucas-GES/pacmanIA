from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador, DirecaoMoverPacman

class AgentePrepostoESHumano(AgenteAbstrato):
    def adquirirPercepcao(self):
        pass
    
    def escolherProximaAcao(self) -> list:
        jogada = None
        while not jogada:
            jogada = input()
            try:
                movimento = AgentePrepostoESHumano.parse_jogada(jogada)
            except ValueError:
                jogada = None
                print('Jogada invalida, digite novamente:')
        return AcaoJogador.mover_pacman(movimento)

    @staticmethod
    def parse_jogada(entrada: str) -> str:
        direcoes = {
            'a': DirecaoMoverPacman.ESQUERDA,
            'd': DirecaoMoverPacman.DIREITA,
            'w': DirecaoMoverPacman.CIMA,
            's': DirecaoMoverPacman.BAIXO
        }
        
        raw_d = entrada
        d = direcoes.get(raw_d.lower())
        if not d:
            raise ValueError()
        return d
        