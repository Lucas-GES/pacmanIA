from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    MOVER_PACMAN = 'MoverPacman'

class DirecaoMoverPacman(Enum):
    DIREITA = 'DIREITA'
    ESQUERDA = 'ESQUERDA'
    CIMA = 'CIMA'
    BAIXO = 'BAIXO'
    
@dataclass
class AcaoJogador():
    tipo: str
    parametros: str
    
    @classmethod
    def mover_pacman(cls, direcao) -> 'AcaoJogador':
        return cls(AcoesJogador.MOVER_PACMAN, (direcao))
    
    