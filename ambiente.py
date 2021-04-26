import os
class Pacman(): 
    jogador = 'C'

    game_over = False

    labirinto = [
            ["_","_","_","_","_","_","_","_","_",],
            ["|","*","#","*","*","*","#","*","|"],
            ["|","*","#","*","#","*","#","*","|"],
            ["|","*","*",".","*","*","*","*","|"],
            ["|",".","*","*","*","*","*","*","|"],
            ["|","*","*","*","#","*","*",".","|"],
            ["|","*","#","*","*","*","#","*","|"],
            ["|","*","*","*","#","*","#","*","|"],
            ["|","*","#",".","*","*","#","*","|"],
            ["-","-","-","-","-","-","-","-","-",],
        ]

    def ambiente(labirinto):        

        for i in range(len(labirinto)):                
            for j in range(len(labirinto[0])):                
                if j == 8:
                    print(labirinto[i][j])
                else:
                    print(str(labirinto[i][j]) + "", end="")

    
    def get_posicao():
        for i in range(len(Pacman.labirinto)):
            for j in range(len(Pacman.labirinto[0])):
                if Pacman.labirinto[i][j] == 'C':
                    x = i
                    y = j
                    return x, y


    def novoJogo():
        jogador = Pacman.jogador

        for i in range(len(Pacman.labirinto)):
            for j in range(len(Pacman.labirinto[0])):
                if i == 6:
                    if  j == 4:
                        Pacman.labirinto[i][j] = jogador
          

    def mover(movimento):
        if movimento == "a":
            for i in range(len(Pacman.labirinto)):
                for j in range(len(Pacman.labirinto[0])):
                    if Pacman.labirinto[i][j] == Pacman.jogador:
                        y = j-1
                        if Pacman.valida_movimento(i, y):
                            Pacman.labirinto[i][y] = Pacman.jogador
                            Pacman.labirinto[i][j] = "*"

        elif movimento == "d":
            for i in range(len(Pacman.labirinto)):
                for j in range(len(Pacman.labirinto[0])):
                    if Pacman.labirinto[i][j] == Pacman.jogador:
                        y = j+1
                        if Pacman.valida_movimento(i, y):
                            Pacman.labirinto[i][y] = Pacman.jogador
                            Pacman.labirinto[i][j] = "*"
                            break
        
        elif movimento == "w":
            for i in range(len(Pacman.labirinto)):
                for j in range(len(Pacman.labirinto[0])):
                    if Pacman.labirinto[i][j] == Pacman.jogador:
                        x = i-1
                        if Pacman.valida_movimento(x, j):
                            Pacman.labirinto[x][j] = Pacman.jogador
                            Pacman.labirinto[i][j] = "*"
                            break

        elif movimento == "s":
            for i in reversed(range(len(Pacman.labirinto))):
                for j in range(len(Pacman.labirinto[0])):
                    if Pacman.labirinto[i][j] == Pacman.jogador:
                        x = i+1
                        if Pacman.valida_movimento(x, j):
                            Pacman.labirinto[x][j] = Pacman.jogador
                            Pacman.labirinto[i][j] = "*"
                            break

    def valida_movimento(x, y):
        if(Pacman.labirinto[x][y] == '#' or Pacman.labirinto[x][y] == '|' or Pacman.labirinto[x][y] == '-' or Pacman.labirinto[x][y] == '_'):
            return False
        else:
            return True
        

if __name__ == '__main__':

    Pacman.novoJogo()
    
    while Pacman.game_over == False:
        os.system('cls||clear')
        Pacman.ambiente(Pacman.labirinto)
        print(Pacman.get_posicao())
        Pacman.mover(input())
        


    


    