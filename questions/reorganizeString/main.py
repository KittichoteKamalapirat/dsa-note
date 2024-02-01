from collections import defaultdict
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)

        maxHeap = [[-val, key] for key,val in counts.items()]

        heapq.heapify(maxHeap)
        prevAndRemaining = None
        print(maxHeap)

        res = ""
        while maxHeap or prevAndRemaining:
            # curr is aba, prev = a, maxheap is []
            # but no other options in maxHeap to select to คั่น
            # so impossible
            if prevAndRemaining and not maxHeap: 
                return ""
                
            cnt, char = heapq.heappop(maxHeap)
        
            res += char
            cnt += 1 # reduce (but plus cause we made negative)

            if prevAndRemaining: # if prev is null => don't add! why add null? lol
                heapq.heappush(maxHeap,prevAndRemaining)
                prevAndRemaining = None

            if cnt != 0: # no need to save as prev which will be added pack to heap later
                prevAndRemaining = [cnt,char]

        return res


# prevAndRemaining means
# aba and there still a remains => mur