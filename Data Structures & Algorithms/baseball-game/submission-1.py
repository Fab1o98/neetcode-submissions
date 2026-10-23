class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Estou guardando pontuações de um jogo de beisebol
        # Regras: 
        # + : Registrar uma nova pontuação com a soma das 2 pontuações anteriores
        # D : Registro uma nova pontuação com o dobro da pontuação anterior
        # C : Anular a última pontuação registrada 
        newResgister = []
        
        for contador in operations: 
            if contador == '+': 
                newResgister.append(newResgister[-1] + newResgister[-2])

            elif contador == 'D': 
                newResgister.append(newResgister[-1] * 2)
        
            elif contador == 'C': 
                newResgister.pop()

            else:
                newResgister.append(int(contador))

        return sum(newResgister)        
