class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr=[]
        for n in arr2:
            new = [i for i in arr1 if i == n]
            for i in new:
                arr.append(i)
            

        old= [i for i in arr1 if i not in arr2] 
        old.sort()
        for n in old:
            arr.append(n)

        return arr