class Pacman(): 
    jogador = ' C '

    labirinto = [
            ["__","__","__","___","___","___","___","___","___",],
            ["|","   "," | ","   ","   ","    ","  | ","   ","|",],
            ["|","   "," | ","   ","----","   ","  | ","   ","|",],
            ["|"," . "," . "," . ","  . "," . ","  . "," . ","|",],
            ["|"," . "," -- ","  ","_  _","   "," -- "," . ","|",],
            ["|"," . ","    ","  ","|__|","   ","    "," . ","|"],
            ["|"," . "," -- ","   ","   "," . "," -- "," . ","|",],
            ["|"," . ","   ","   ","____"," . "," . ","  . ","|",],
            ["|","   "," | ","   ","    ","   ","  | ","   ","|",],
            ["---","---","---","---","---","-","---","---","---",],
        ]

    def ambiente(labirinto):        

        for i in range(len(labirinto)):                
            for j in range(len(labirinto[0])):                
                if j == 8:
                    print(labirinto[i][j])
                else:
                    print(str(labirinto[i][j]) + "", end="")
                    
    def novoJogador():
        jogador = ' C '
        return jogador

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
                        a = j-1
                        Pacman.labirinto[i][a] = Pacman.jogador
                        Pacman.labirinto[i][j] = "   "
        

if __name__ == '__main__':

    Pacman.novoJogo()
    Pacman.ambiente(Pacman.labirinto)
    Pacman.mover(input())
    Pacman.ambiente(Pacman.labirinto)  


    


    