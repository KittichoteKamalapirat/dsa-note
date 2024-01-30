# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def recurse(arr,s,e):
            if e - s +1 <= 1:
                return

            pivot = arr[e]
            pointer = s

            for i in range(s,e):
                if arr[i].key < pivot.key:
                    tmp = arr[i]
                    arr[i] = arr[pointer]
                    arr[pointer] = tmp
                    pointer += 1
            
            
            arr[e] = arr[pointer]
            arr[pointer] = pivot
            
            # sort left
            recurse(arr,s,pointer-1)
            
            # sort right
            recurse(arr,pointer+1,e)

        recurse(pairs, 0, len(pairs)-1)
        return pairs
        