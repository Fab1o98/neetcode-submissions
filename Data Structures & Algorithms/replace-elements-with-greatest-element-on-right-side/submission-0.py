class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # inicial máximo = -1 
        # Iteração reversa 
        # novo máximo = max(maximoAntigo, arr[i])

        maximoDireita = -1 
        for i in range(len(arr) -1, -1, -1):
            novoMaximo = max(maximoDireita, arr[i])
            arr[i] = maximoDireita
            maximoDireita = novoMaximo
        return arr