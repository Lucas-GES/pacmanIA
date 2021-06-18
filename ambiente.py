
class Ambiente():            
        labirinto_completo = [
            ["█","█","█","█","█","█","█","█","█","█","█","█"],
            ["█"," "," "," "," "," "," "," "," "," ",".","█"],
            ["█"," "," "," ","█","█","█"," "," ","█"," ","█"],
            ["█"," ","█"," "," "," "," "," ","█","█"," ","█"],
            ["█"," "," "," "," "," "," "," "," "," "," ","█"],
            ["█"," ","█"," ","█"," ","█"," ","█"," "," ","█"],
            ["█"," ","█"," ","█","█","█"," ","█"," "," ","█"],
            ["█"," "," "," "," ","█"," "," "," "," "," ","█"],
            ["█"," "," ","█"," "," "," ","█"," ","█"," ","█"],
            ["█","█","█","█","█","█","█","█","█","█","█","█"],
        ]
        labirinto = labirinto_completo        
        acoes_personagens = {0: None}        
        jogador = 'c'         
    
        def get_jogador() -> tuple[int, int]:
            for i in range(len(Ambiente.labirinto)):
                for j in range(len(Ambiente.labirinto[0])):
                    if Ambiente.labirinto[i][j] == 'c':
                        x = i
                        y = j
                        return x, y

        def get_ponto() -> tuple[int, int]:
            for i in range(len(Ambiente.labirinto)):
                for j in range(len(Ambiente.labirinto[0])):
                    if Ambiente.labirinto[i][j] == '.':
                        x = i
                        y = j
                        return x, y

        def game_over():
            count = 0
            for i in range(len(Ambiente.labirinto)):
                for j in range(len(Ambiente.labirinto[0])):
                    if Ambiente.labirinto[i][j] == ".":
                        count += 1

            if count == 0:
                return True
            else:
                return False

        def get_labirinto():
            return Ambiente.labirinto

        def inserirJogador():
        
            for i in range(len(Ambiente.labirinto)):
                for j in range(len(Ambiente.labirinto[0])):
                    if i == 8:
                        if j == 5:
                            Ambiente.labirinto[i][j] = Ambiente.jogador
    
        def print_labirinto():
            for i in range(len(Ambiente.labirinto)):                
                for j in range(len(Ambiente.labirinto[0])):                
                    if j == 11:
                        print(Ambiente.labirinto[i][j])
                    else:
                     print(str(Ambiente.labirinto[i][j]) + "", end="")