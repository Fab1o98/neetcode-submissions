class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # O que eu quero retornar? 
        # O valor de numeros que existem no meu array tirando o numero que foi me passado como valor.

        qtdArray = 0 

        for i in range(len(nums)):
            if nums[i] != val: 
                nums[qtdArray] = nums[i]
                qtdArray += 1
        return qtdArray 
