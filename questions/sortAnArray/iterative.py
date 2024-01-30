class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, start, mid, end):
            temp = []
            i, j = start, mid + 1

            while i <= mid and j <= end:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            while i <= mid:
                temp.append(arr[i])
                i += 1

            while j <= end:
                temp.append(arr[j])
                j += 1

            for i in range(len(temp)):
                arr[start + i] = temp[i]

        n = len(nums)
        curr_size = 1

        while curr_size < n:
            for start in range(0, n, curr_size * 2):
                mid = min(start + curr_size - 1, n-1)
                end = min(start + 2 * curr_size - 1, n-1)
                merge(nums, start, mid, end)

            curr_size *= 2

        return nums