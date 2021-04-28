from ambiente import Ambiente

class Acoes():
    def mover(movimento):
        if movimento == "a":
            for i in range(len(Ambiente.labirinto)):
                for j in range(len(Ambiente.labirinto[0])):
                    if Ambiente.labirinto[i][j] == Ambiente.jogador:
                        y = j-1
                        if Acoes.valida_movimento(i, y):
                            Ambiente.labirinto[i][y] = Ambiente.jogador
                            Ambiente.labirinto[i][j] = "*"

        elif movimento == "d":
            for i in range(len(Ambiente.labirinto)):
                for j in range(len(Ambiente.labirinto[0])):
                    if Ambiente.labirinto[i][j] == Ambiente.jogador:
                        y = j+1
                        if Acoes.valida_movimento(i, y):
                            Ambiente.labirinto[i][y] = Ambiente.jogador
                            Ambiente.labirinto[i][j] = "*"
                            break
        
        elif movimento == "w":
            for i in range(len(Ambiente.labirinto)):
                for j in range(len(Ambiente.labirinto[0])):
                    if Ambiente.labirinto[i][j] == Ambiente.jogador:
                        x = i-1
                        if Acoes.valida_movimento(x, j):
                            Ambiente.labirinto[x][j] = Ambiente.jogador
                            Ambiente.labirinto[i][j] = "*"
                            break

        elif movimento == "s":
            for i in reversed(range(len(Ambiente.labirinto))):
                for j in range(len(Ambiente.labirinto[0])):
                    if Ambiente.labirinto[i][j] == Ambiente.jogador:
                        x = i+1
                        if Acoes.valida_movimento(x, j):
                            Ambiente.labirinto[x][j] = Ambiente.jogador
                            Ambiente.labirinto[i][j] = "*"
                            break

    def valida_movimento(x, y):
        if(Ambiente.labirinto[x][y] == '#' or Ambiente.labirinto[x][y] == '|' or Ambiente.labirinto[x][y] == '-' or Ambiente.labirinto[x][y] == '_'):
            return False
        else:
            return True
