class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        pares = {")": "(", "]": "[", "}": "{"}
        
        for c in s:
            
            # Se c for de abertura, como colocamos na pilha?
            # Se c for de fechamento, como checamos o topo da pilha?
            if c in pares:    
                # Preciso ver se a pilha está vazia ou mostrar o topo e ver se é diferente de pares
                #if pilha[c] == 0 or pilha[-1] ===> O que está errado aqui?? Quero ver o tamanho da pilha, nesse caso estou falando pilha[aqui vai mostrar o que está no índice]
                if len(pilha) == 0 or pilha[-1] != pares[c]:
                    return False 
                pilha.pop()
            else: 
                pilha.append(c)
                
        return len(pilha) == 0
                