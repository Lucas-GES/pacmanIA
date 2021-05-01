import queue
from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador, DirecaoMoverPacman


class AgenteAutomaticoBfs(AgenteAbstrato):
    
    movimentos = []
    movimento = ""

    def get_movimentos(self):
        return self.movimentos

    def set_movimento(self, movimento):
        self.movimento = movimento

    def adquirirPercepcao(self):
        pass

    def get_bfs(self):
        global labirinto
        labirinto = [
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
        fila = queue.Queue()
        fila.put("")
        add = ""
        while not self.atualizarEstado(add):
            add = fila.get()
            for i in ["a", "d", "w", "s"]:
                put = add + i
                if self.valida_movimento(put):
                    fila.put(put)

    def escolherProximaAcao(self):
        try:
            movimento = AgenteAutomaticoBfs.parse_jogada(self.movimento)
        except ValueError:
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

    # def achou_solucao(self) -> bool:
    #     count = 0
    #     for i in range(len(labirinto)):
    #         for j in range(len(labirinto[0])):
    #             if labirinto[i][j] == ".":
    #                 count += 1

    #     if count == 0:
    #         return True
    #     else:
    #         return False

    def atualizarEstado(self, moves):
        i = 5
        j = 8
        
        for move in moves:
            if move == 'a':
                i -= 1
            elif move == "d":
                i += 1

            elif move == "w":
                j -= 1

            elif move == "s":
                j += 1

        if labirinto[j][i] == ".":
            self.movimentos = moves
            return True

        return False

    def valida_movimento(self, moves):

        i = 5
        j = 8
        
        for move in moves:
            if move == 'a':
                i -= 1
            elif move == "d":
                i += 1

            elif move == "w":
                j -= 1

            elif move == "s":
                j += 1

            if not(0 <= i < len(labirinto[0]) and 0 <= j < len(labirinto)):
                return False
            elif (labirinto[j][i] == "█"):
                return False

        return True