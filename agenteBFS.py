from ambiente import Ambiente
from actions import Actions
import queue
import os
import time

class AgenteBFS():   
    
    movimentos = []
    movimento = ""
    labirinto = Ambiente.labirinto_completo

    def get_movimentos():
        return self.movimentos

    def set_movimento(movimento):
        AgenteBFS.movimento = movimento           
    
    
    def valid(moves):        
        i = 5
        j = 8
        for move in moves:
            if move == "a":
                i -= 1

            elif move == "d":
                i += 1

            elif move == "w":
                j -= 1

            elif move == "s":
                j += 1

            if not(0 <= i < len(AgenteBFS.labirinto[0]) and 0 <= j < len(AgenteBFS.labirinto)):
                return False
            elif (AgenteBFS.labirinto[j][i] == "█"):
                return False

        return True


    def findEnd(moves):      
        i = 5
        j = 8

        for move in moves:
            if move == "a":
                i -= 1

            elif move == "d":
                i += 1

            elif move == "w":
                j -= 1

            elif move == "s":
                j += 1

        if AgenteBFS.labirinto[j][i] == ".":            
            AgenteBFS.movimentos = list(moves)                        
            return True

        return False
  

    def exec():

        nums = queue.Queue()
        nums.put("")
        add = ""
        
        while not AgenteBFS.findEnd(add) : 
            add = nums.get()            
            for j in ["a", "d", "w", "s"]:
                put = add + j                                   
                if AgenteBFS.valid(put):
                    nums.put(put)


        for i in AgenteBFS.movimentos:
            Actions.atualizarEstado(i)                   
            os.system('cls||clear')
            Ambiente.print_labirinto()
            time.sleep(0.5)
        
        Ambiente.print_labirinto()
        print(f"Found: {AgenteBFS.movimentos}")
        
                