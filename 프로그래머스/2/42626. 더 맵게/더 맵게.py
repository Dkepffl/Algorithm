import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(len(scoville)>1):
        x1 = heapq.heappop(scoville)
        if x1 >= K:
            return answer
        else:
            x2=heapq.heappop(scoville)
            heapq.heappush(scoville, x1+2*x2)
            answer+=1
    if scoville[0]<K:
        return -1
    return answer