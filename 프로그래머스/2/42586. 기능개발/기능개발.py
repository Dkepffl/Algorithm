import math

def solution(progresses, speeds):
    ans=[]
    dday=[] # 배포 D-day
    for i in range(len(progresses)):
        dday.append(math.ceil((100-progresses[i])/speeds[i]))
    
    while(sum(ans)!=len(dday)):
        cnt=1
        for i in range(sum(ans)+1,len(dday)):
            if dday[i]<=dday[sum(ans)]:cnt+=1
            else : break
        ans.append(cnt)

    return ans