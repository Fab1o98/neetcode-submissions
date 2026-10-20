class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Para concatenar uma matriz de forma simples posso passar por ela 2 vezes e atribuir o valor de cada indice. 

        ans = []

        for i in range(2):
            for i in nums: 
                ans.append(i)
        return ans