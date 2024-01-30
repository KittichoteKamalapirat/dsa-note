class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr,s,e):
            if e <= s: # e could be -1 when input is []
                return

            # divide
            m = (s+e )// 2

            mergeSort(arr,s,m)
            mergeSort(arr,m+1,e)

            # conquer
            merge(arr,s,m,e)


        def merge(arr,s,m,e):
            left = arr[s:m+1]
            right = arr[m+1:e+1] # e+1

            i = s
            pointer1 = 0
            pointer2 = 0

            while pointer1 < len(left) and pointer2 < len(right):
                if left[pointer1] <= right[pointer2]:
                    arr[i] = left[pointer1]
                    pointer1 += 1
                else:
                    arr[i] = right[pointer2]
                    pointer2 += 1
                i += 1

            while pointer1 < len(left):
                arr[i] = left[pointer1]
                pointer1 += 1
                i += 1

            while pointer2 < len(right):
                arr[i] = right[pointer2]
                pointer2 += 1
                i += 1
                
            
        mergeSort(nums,0,len(nums)-1)

        return nums