from ambiente import Ambiente


class Actions():
    

    def valida_movimento(x, y):
        if(Ambiente.labirinto[x][y] == '█'):
            return False
        else:
            return True

    def atualizarEstado(jogada):              
        
            if jogada == 'a':
                for i in range(len(Ambiente.labirinto)):
                    for j in range(len(Ambiente.labirinto[0])):
                        if Ambiente.labirinto[i][j] == Ambiente.jogador:
                            y = j-1
                            if Actions.valida_movimento(i, y):
                                Ambiente.labirinto[i][y] = Ambiente.jogador
                                Ambiente.labirinto[i][j] = " "

            elif jogada == "d":
                for i in range(len(Ambiente.labirinto)):
                    for j in range(len(Ambiente.labirinto[0])):
                        if Ambiente.labirinto[i][j] == Ambiente.jogador:
                            y = j+1
                            if Actions.valida_movimento(i, y):
                                Ambiente.labirinto[i][y] = Ambiente.jogador
                                Ambiente.labirinto[i][j] = " "
                                break
            
            elif jogada == "w":
                for i in range(len(Ambiente.labirinto)):
                    for j in range(len(Ambiente.labirinto[0])):
                        if Ambiente.labirinto[i][j] == Ambiente.jogador:
                            x = i-1
                            if Actions.valida_movimento(x, j):
                                Ambiente.labirinto[x][j] = Ambiente.jogador
                                Ambiente.labirinto[i][j] = " "
                                break

            elif jogada == "s":
                for i in reversed(range(len(Ambiente.labirinto))):
                    for j in range(len(Ambiente.labirinto[0])):
                        if Ambiente.labirinto[i][j] == Ambiente.jogador:
                            x = i+1
                            if Actions.valida_movimento(x, j):
                                Ambiente.labirinto[x][j] = Ambiente.jogador
                                Ambiente.labirinto[i][j] = " "
                                break