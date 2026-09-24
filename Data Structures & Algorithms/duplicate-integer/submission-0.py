class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visitado = set()
        for visto in nums: 
            if visto in visitado:
                return True
            else: 
                visitado.add(visto)
        return False
