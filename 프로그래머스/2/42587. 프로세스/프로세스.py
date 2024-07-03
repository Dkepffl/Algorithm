def solution(priorities, location):
    answer=0
    queue = [[i, priorities[i]] for i in range(len(priorities))]
    while True:
        max_p = max(priorities)
        if queue[0][1]==max_p:
            if queue[0][0]==location:
                return answer+1
            else:
                priorities.remove(queue[0][1])
                queue.pop(0)
                answer+=1
        elif queue[0][1]!=max_p:
            cur = queue.pop(0)
            queue.append(cur)
