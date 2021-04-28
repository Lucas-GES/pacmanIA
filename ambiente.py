
class Ambiente(): 
    jogador = 'c'

    game_over = False

    labirinto = [
            ["_","_","_","_","_","_","_","_","_",],
            ["|"," ","|"," "," "," ","|"," ","|"],
            ["|","_",".","_","_","_"," ","_","|"],
            ["|","|","."," "," "," "," ","|","|"],
            ["|"," ","."," "," "," "," "," ","|"],
            ["|","|",".","_"," ","_"," ","|","|"],
            ["|","-",".","|","_","|"," ","-","|"],
            ["|"," ",".",".","_"," "," "," ","|"],
            ["|"," ","|","."," "," ","|"," ","|"],
            ["_","_","_","_","_","_","_","_","_",],
        ]

    def ambiente(labirinto):        

        for i in range(len(labirinto)):                
            for j in range(len(labirinto[0])):                
                if j == 8:
                    print(labirinto[i][j])
                else:
                    print(str(labirinto[i][j]) + "", end="")

    
    def get_posicao():
        for i in range(len(Ambiente.labirinto)):
            for j in range(len(Ambiente.labirinto[0])):
                if Ambiente.labirinto[i][j] == 'c':
                    x = i
                    y = j
                    return x, y
  
    
    

   


    


    