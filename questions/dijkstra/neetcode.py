class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}

        for i in range(n):
            adj[i] = []

        
        for s,d,w in edges:
            adj[s].append((w,d))


        res = {}        
        minHeap = [(0,src)]
        heapq.heapify(minHeap)

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in res:
                # need to check this because there could be multiple n1 in heap, 
                # but the first one added will be the shortest one
                continue 

            res[n1] = w1

            for w2,n2 in adj[n1]:
                if n2 not in res: # probably not need this line, since it won't be updated again anyway. check to save space

                    heapq.heappush(minHeap,(w2+w1,n2))

        for i in range(n):
            if i not in res:
                res[i] = -1
        
        return res

